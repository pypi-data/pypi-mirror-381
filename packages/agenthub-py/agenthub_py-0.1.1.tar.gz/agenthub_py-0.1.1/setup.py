"""
Setup configuration for AgentHub package.
"""

from setuptools import setup, find_packages

with open("agenthub/README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agenthub-py",
    version="0.1.1",
    author="Youssef Kallel",
    author_email="youssef@agenthublabs.com",
    description="A framework for running AI agents on AgentHub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://agenthublabs.com",
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
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=5.0",
            "mypy>=1.0",
        ]
    },
)