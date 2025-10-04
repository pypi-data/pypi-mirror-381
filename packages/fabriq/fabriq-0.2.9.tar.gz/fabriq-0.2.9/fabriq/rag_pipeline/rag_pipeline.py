from fabriq.llm import LLM
from fabriq.retriever import VectorRetriever
from fabriq.reranking import Reranker
from typing import List, Dict, Any
from langchain.schema import Document


class RAGPipeline:
    def __init__(self, config):
        """Initialize the RAG pipeline with an LLM model, retriever, and prompt template."""
        self.config = config
        self.llm = LLM(self.config)
        self.retriever = VectorRetriever(self.config)
        if self.config.get("reranker").get("type")!="none":
            self.reranker = Reranker(self.config)
        else:
            self.reranker = None
        # self.prompt_template = "You are a helpful AI assistant. Based on the following context, answer the question. DO NOT MAKE UP YOUR OWN ANSWER, ANSWER USING THE GIVEN CONTEXT ONLY. \n\n{documents}\n\nQuestion: {query}\nAnswer:"
        self.prompt_template: str = (
            self.config.get("prompts").get("params").get("rag_prompt", None)
        )

    def is_query_relevant(self, query: str, documents: List[Document]) -> bool:
        """Check if the query is relevant to the retrieved documents."""
        system_prompt = "Your task is to determine if the query is relevant to the provided documents in a RAG pipeline. Respond with either 'True' or 'False' strictly."
        prompt = f"Documents: {documents}\n\nQuery: {query}"
        response = self.llm.generate(prompt, system_prompt=system_prompt)
        return True if "true" in response.lower() else False

    def query_rewrite(self, query: str) -> str:
        """Rewrites the query to get better retrieval."""
        prompt = f"""You are an expert search query optimizer for a Retrieval-Augmented Generation (RAG) system.
        Your task:
        Given the user's original query, rewrite it into a single, well-formed, search-optimized query that:
        - Preserves the original meaning and intent.
        - Uses clear, unambiguous language.
        - Includes relevant keywords and synonyms that improve retrieval.
        - Expands abbreviations or acronyms if needed and write the original abbreviation in bracket after it.
        - Matches the style of queries that would return the most relevant results from a mixed keyword + semantic search system.

        Return only the rewritten query as plain text — no explanations.

        Example:
        Original Query: "best EV range"
        Rewritten Query: "electric vehicles (EV) with the longest driving range"

        Original Query: "{query}"
        Rewritten Query:
        """
        return self.llm.generate(prompt).strip()

    def get_response(self, query: str, filter=None) -> str:
        """Run the RAG pipeline to retrieve relevant documents and generate a response."""
        if not self.prompt_template:
            raise ValueError("Prompt is not set.")
        if not self.llm:
            raise ValueError("LLM model is not initialized.")

        rewritten_query = self.query_rewrite(query)
        top_k = self.config.get("retriever").get("params").get("top_k", 15)
        documents = self.retriever.retrieve(rewritten_query, top_k=top_k, filter=filter)
        if self.reranker:
            documents = self.reranker.rerank(rewritten_query, documents)
        documents = documents[:top_k]

        if not documents:
            return {
                "text": "No relevant documents found.",
                "chunks": [],
                "metadata": [],
            }

        # Format the retrieved documents for the prompt
        documents_content = "\n\n----------\n\n".join([doc.page_content for doc in documents])

        fallback_response = (
            self.config.get("prompts")
            .get("params")
            .get(
                "fallback_response",
                "I cannot find relevant information to answer your question. Please ask your question relevant to the documents or rephrase it.",
            )
        )

        # Check if the query is relevant to the retrieved documents
        if self.is_query_relevant(rewritten_query, documents_content) is False:
            result = {
                "text": fallback_response,
                "chunks": [],
                "metadata": [],
            }

        else:
            # Prepare the prompt with retrieved documents
            prompt = self.prompt_template.format(
                query=rewritten_query, context=documents_content
            )

            # Generate a response using the LLM model
            response = self.llm.generate(prompt)

            result = {
                "text": response if response else fallback_response,
                "chunks": documents,
                "metadata": (
                    [getattr(doc, "metadata", {}) for doc in documents]
                    if response
                    else []
                ),
            }
        return result
