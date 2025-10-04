from setuptools import setup, find_packages

with open("requirements.txt", "r") as file:
    common_requirements = [line.strip() for line in file]

with open("packages/doc-loader.txt", "r") as file:
    doc_loader = [line.strip() for line in file]

with open("packages/index.txt", "r") as file:
    index = [line.strip() for line in file]

with open("packages/rag.txt", "r") as file:
    rag = [line.strip() for line in file]

with open("packages/tools.txt", "r") as file:
    tools = [line.strip() for line in file]

with open("packages/evals.txt", "r") as file:
    evals = [line.strip() for line in file]

all = list(set(common_requirements + doc_loader + index + rag+ tools + evals))

setup(
    name="fabriq",
    version="0.2.9",
    description="Fabriq is a Python SDK for developing quick, low code, and enterprise-level Generative AI solutions.",
    author="Aaryan Verma",
    url="https://github.com/Aaryanverma/fabriq",
    packages=find_packages(),
    install_requires=common_requirements,
    include_package_data=True,
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
    ],
    extras_require={
        'doc-loader': doc_loader,
        'index': index,
        'rag': rag,
        'tools': tools,
        'evals': evals,
        'all': all
    }
)