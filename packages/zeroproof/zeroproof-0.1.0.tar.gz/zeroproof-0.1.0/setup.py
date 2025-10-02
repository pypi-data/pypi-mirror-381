"""
Setup configuration for ZeroProof Python SDK
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

setup(
    name="zeroproof",
    version="0.1.0",
    author="ZeroProof AI",
    author_email="support@zeroproofai.com",
    description="Python SDK for ZeroProof AI verification API - Secure your agentic e-commerce ecosystem",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/jacobweiss2305/zeroproof",
    project_urls={
        "Bug Tracker": "https://github.com/jacobweiss2305/zeroproof/issues",
        "Documentation": "https://docs.zeroproofai.com",
        "Source Code": "https://github.com/jacobweiss2305/zeroproof",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Security :: Cryptography",
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
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "twine>=4.0.0",
        ],
    },
    keywords="zeroproof ai verification zkp zero-knowledge-proof agent security ecommerce",
    license="MIT",
)
