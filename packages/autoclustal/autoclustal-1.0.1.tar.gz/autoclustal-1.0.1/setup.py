#!/usr/bin/env python3
"""
Setup script for AutoClustal - Comprehensive Bioinformatics Pipeline
"""

from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="autoclustal",
    version="1.0.0",
    author="Stella Hartono",
    author_email="srhartono@users.noreply.github.com",
    description="Comprehensive bioinformatics pipeline for sequence analysis, clustering, phylogeny, and BLAST annotation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srhartono/autoclustal",
    project_urls={
        "Bug Tracker": "https://github.com/srhartono/autoclustal/issues",
        "Documentation": "https://github.com/srhartono/autoclustal#readme",
        "Source Code": "https://github.com/srhartono/autoclustal",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "autoclustal=autoclustal.bin.autoclustal:main",
            "autoclustal-visualize=autoclustal.bin.visualize:main",
            "autoclustal-grapher=autoclustal.bin.grapher:main",
        ],
    },
    keywords="bioinformatics phylogeny clustering blast sequence-analysis alignment",
    include_package_data=True,
    package_data={
        "autoclustal": ["conf/*", "*.md", "*.txt"],
    },
)