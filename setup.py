#! /usr/bin/env python3
from setuptools import setup, find_packages
import pathlib

setup(
    name                =   "apidocs",
    description         =   "Collection of API documentations generated with pydoctor",
    url                 =   "https://github.com/tristanlatr/apidocs",
    version             =   "0.dev",
    classifiers         =   ["Programming Language :: Python :: 3"],
    license             =   "MIT LICENSE",
    long_description    =   pathlib.Path(__file__).parent.joinpath("README.md").read_text(),
    long_description_content_type   =   "text/markdown",
    )
