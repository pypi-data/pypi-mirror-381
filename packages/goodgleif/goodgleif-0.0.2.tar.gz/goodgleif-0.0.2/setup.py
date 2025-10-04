#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="goodgleif",
    version="0.0.2",
    description="Lightweight tools for working with GLEIF LEI data: preprocess, load, fuzzy query.",
    author="Peter Cotton",
    python_requires=">=3.9",
    packages=find_packages(include=["goodgleif", "goodgleif.*"]),
    install_requires=[
        "pandas>=2.1",
        "pyarrow>=14.0",
        "rapidfuzz>=3.6",
        "platformdirs>=4.2",
        "pyyaml>=6.0.1",
    ],
    extras_require={
        "polars": ["polars>=1.8"],
        "dev": ["pytest>=7.4", "ruff>=0.5.0"],
    },
    include_package_data=True,   # works with MANIFEST.in for sdists
    entry_points={
        "console_scripts": [
            "goodgleif=goodgleif.cli:main",
        ],
    },
)
