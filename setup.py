#!/usr/bin/env python

import os
from setuptools import setup, find_packages
__version__ = "0.1"


scripts = ["bin/" + j for j in os.listdir("bin") ]

requires = [
    "numpy",
    "astropy",
    "argparse"
]


setup(name = "pyddi",
    version = __version__,
    description = "Identifies Sources that Require Direction-Dependent Calibration.",
    author = "Lerato Sebokolodi",
    author_email = "mll.sebokolodi@gmail.com",
    url = "https://github.com/Sebokolodi/pyddi",
    packages = find_packages(),
    install_requires = requires,
    scripts = scripts, 
    dependency_links=['https://github.com/o-smirnov/tigger.git'],
    license = "GNU GPL v2",
    classifiers = [],
 )

