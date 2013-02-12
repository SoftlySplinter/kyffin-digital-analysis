#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name = "kyffin",
    version = "0.1",
    author = "Alexander D Brown",
    author_email = "alex@alexanderdbrown.com",
    url = "",
    description = "Kyffin Williams: Digital Analysis of Paintings",
    long_description = open('README.md').read(),

    # Packages
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    
    entry_points = {
        'console_scripts': ['kyffin = kyffin.cli:main']
    },

    # Requirements
    install_requires = [
        'matplotlib',
        'scipy',
        'liac-arff',
    ],

    test_suite = "kyffin.tests",
)
