import os
import sys
from setuptools import setup

DESCRIPTION = 'Utility functions to make publication quality figures.'
VERSION = '0.0.0-alpha'


setup(
    name="plotmastery",
    version=VERSION,
    author="Nelle Varoquaux",
    author_email="nelle.varoquaux@gmail.com",
    description=DESCRIPTION,
    license = "BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
