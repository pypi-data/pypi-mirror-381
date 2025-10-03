#!/usr/bin/env python3
"""
Setup script for ABIDE Data Explorer package.
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="abide-data-explorer",
    version="1.0.0",
    author="Data Explorer Team",
    author_email="contact@example.com",
    description="A Streamlit application for exploring ABIDE II Composite Phenotypic data",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/ItsHarshitAg/lab10",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=read_requirements(),
    include_package_data=True,
    package_data={
        "abide_data_explorer": ["data/*.csv"],
    },
    entry_points={
        "console_scripts": [
            "abide-data-explorer=abide_data_explorer.cli:main",
        ],
    },
    keywords="data analysis, streamlit, abide, neuroscience, visualization",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/abide-data-explorer/issues",
        "Source": "https://github.com/yourusername/abide-data-explorer",
    },
)