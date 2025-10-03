"""
Setup script for SanTOK package
"""

from setuptools import setup, find_packages
import os

def read_readme():
    """Read the README file"""
    readme_path = os.path.join(os.path.dirname(__file__), 'FULL_README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "SanTOK - Advanced Multi-Format Tokenization System"

def get_version():
    return "1.0.6"

setup(
    name="santok",
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
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    entry_points={
        "console_scripts": [
            "santok=santok:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "tokenization", "nlp", "text-processing", "numerology", 
        "hashing", "compression", "embeddings", "ai", "machine-learning"
    ],
    download_url="https://github.com/chavalasantosh/santok/archive/v1.0.0.tar.gz",
)