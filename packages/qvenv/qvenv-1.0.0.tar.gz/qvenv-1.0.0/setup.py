#!/usr/bin/env python3

from setuptools import setup
import os

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="qvenv",
    version="1.0.0",
    author="Griffin Strier",
    author_email="griffin@gsuite.dev",
    description="A command-line tool for managing Python virtual environments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GriffinCanCode/QVenv",
    py_modules=["qvenv"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "qvenv=qvenv:main",
        ],
    },
    keywords="virtualenv venv environment python packaging development",
    project_urls={
        "Bug Reports": "https://github.com/GriffinCanCode/QVenv/issues",
        "Source": "https://github.com/GriffinCanCode/QVenv",
    },
)

