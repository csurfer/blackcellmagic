#!/usr/bin/env python
from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.rst")) as f:
    long_description = f.read()

setup(
    # Name of the module
    name="blackcellmagic",
    # Details
    version="0.0.2",
    description="IPython wrapper to format cell using black.",
    long_description=long_description,
    # The project's main homepage.
    url="https://github.com/csurfer/blackcellmagic",
    # Author details
    author="Vishwas B Sharma",
    author_email="sharma.vishwas88@gmail.com",
    # License
    license="MIT",
    py_modules=["blackcellmagic"],
    keywords="automation formatter yapf autopep8 pyfmt gofmt rustfmt IPython",
    classifiers=[
        # Intended Audience.
        "Intended Audience :: Developers",
        # Environment.
        "Environment :: Console",
        # License.
        "License :: OSI Approved :: MIT License",
        # Project maturity.
        "Development Status :: 3 - Alpha",
        # Operating Systems.
        "Operating System :: OS Independent",
        # Supported Languages.
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        # Topic tags.
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    install_requires=["black", "ipython"],
)
