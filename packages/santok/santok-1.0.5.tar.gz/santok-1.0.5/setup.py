#!/usr/bin/env python3
"""
SanTOK (Sanitized Tokenization) - Advanced Multi-Format Tokenization System
Setup script for PyPI distribution
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'FULL_README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "SanTOK - Advanced Multi-Format Tokenization System"

# Read version from the package
def get_version():
    return "1.0.5"

setup(
    name="santok-tokenizer",
    version=get_version(),
    author="Santosh chavala",
    author_email="chavalasantosh@hotmail.com",
    description="Advanced multi-format tokenization system with numerology, hashing, compression, and embeddings",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/chavalasantosh/santok",
    project_urls={
        "Bug Tracker": "https://github.com/chavalasantosh/santok/issues",
        "Documentation": "https://github.com/chavalasantosh/santok/tree/main/docs",
        "Source Code": "https://github.com/chavalasantosh/santok",
    },
    packages=find_packages(),
    classifiers=[
        # Development Status
        "Development Status :: 5 - Production/Stable",
        
        # Intended Audience
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        
        # Topic
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        
        # License
        "License :: OSI Approved :: MIT License",
        
        # Programming Language
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        
        # Operating System
        "Operating System :: OS Independent",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        
        # Environment
        "Environment :: Console",
        "Environment :: Other Environment",
        
        # Natural Language
        "Natural Language :: English",
    ],
    keywords=[
        "tokenization", "nlp", "text-processing", "numerology", "hashing", 
        "compression", "embeddings", "concurrent-processing", "text-analysis",
        "pattern-recognition", "anomaly-detection", "reconstruction", "bpe",
        "subword", "character-level", "word-level", "syllable", "frequency",
        "fnv", "murmur", "cityhash", "xxhash", "lz77", "huffman", "rle"
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - pure Python implementation
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=0.5",
            "myst-parser>=0.15",
        ],
        "performance": [
            "psutil>=5.8",  # For memory monitoring
            "numpy>=1.20",  # For advanced numerical operations (optional)
        ],
    },
    entry_points={
        "console_scripts": [
            "santok=santok:main",
            "santok-cli=santok:main",
        ],
    },
    include_package_data=True,
    package_data={
        "santok": [
            "*.md",
            "docs/*.md",
        ],
    },
    zip_safe=False,
    
    # Additional metadata
    platforms=["any"],
    license="MIT",
    
    # PyPI metadata
    download_url="https://github.com/chavalasantosh/santok/archive/v1.0.0.tar.gz",
)
