#!/usr/bin/env python
"""
Setup script for mongodb-query-builder.

This file is provided for backward compatibility with older build tools.
Modern installations should use pyproject.toml.
"""

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# All configuration is in pyproject.toml
# This file is kept for backward compatibility only
setup(
    long_description=long_description,
    long_description_content_type="text/markdown",
)