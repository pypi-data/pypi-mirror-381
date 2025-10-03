"""Setup configuration for DSA Toolkit."""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dsa-toolkit",
    version="1.0.1",
    author="Masoom Verma",
    author_email="0xmasoom@gmail.com",
    description="A comprehensive toolkit for Data Structures and Algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/masoomverma/dsa-toolkit",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    keywords="data-structures algorithms dsa sorting searching graphs trees",
    project_urls={
        "Bug Reports": "https://github.com/masoomverma/dsa-toolkit/issues",
        "Source": "https://github.com/masoomverma/dsa-toolkit",
        "Documentation": "https://github.com/masoomverma/dsa-toolkit#readme",
    },
)
