#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   Acerca de AutoDoc Project (https://github.com/juniors90/notasautodoc/).
# Copyright (c) 2020, Juan David Ferreira
# License: MIT
#   Full Text: https://github.com/juniors90/notasautodoc/blob/main/LICENSE

# =====================================================================
# DOCS
# =====================================================================

"""This file is for distribute Acerca de AutoDoc"""

# ======================================================================
# IMPORTS
# ======================================================================

import os
import pathlib

from setuptools import setup  # noqa

# =============================================================================
# CONSTANTS
# =============================================================================

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))


REQUIREMENTS = []

with open(PATH / "docs" / "source" / "conf.py") as fp:
    for line in fp.readlines():
        if line.startswith("release = "):
            VERSION = line.split("=", 1)[-1].replace('"', "").strip()
            break


with open("README.rst") as fp:
    LONG_DESCRIPTION = fp.read()


# =============================================================================
# FUNCTIONS
# =============================================================================

setup(
    name="AutoDocs",
    version=VERSION,
    description="Acerca de AutoDoc",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/x-rst",
    author="Ferreira, Juan David",
    author_email="juniors9a0@gmail.com",
    url="https://github.com/juniors90/notasautodoc",
    packages=[],
    license="The MIT License",
    install_requires=REQUIREMENTS,
    keywords=["GAP Programming Language", "Groups", "AutoDoc Package"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
    ],
)