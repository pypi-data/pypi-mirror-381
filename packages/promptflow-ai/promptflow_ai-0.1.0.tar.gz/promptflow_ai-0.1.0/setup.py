from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="promptflow-ai",
    version="0.1.0",
    author="PromptFlow",
    author_email="hello@promptflow.dev",
    description="Agentic AI infrastructure for tracking LLM performance and prompt accuracy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/promptflow/promptflow-ai",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.25.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "mypy>=0.950",
        ],
    },
    keywords="ai agentic-ai llm prompts tracking analytics openai anthropic monitoring",
    project_urls={
        "Documentation": "https://promptflow-ui.vercel.app",
        "Source": "https://github.com/promptflow/promptflow-ai",
        "Bug Reports": "https://github.com/promptflow/promptflow-ai/issues",
    },
)
