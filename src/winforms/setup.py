#!/usr/bin/env python
import re

from setuptools import setup

# Version handline needs to be programatic because
# we can't import toga_winforms to compute the version;
# and to support versioned subpackage dependencies
with open('toga_winforms/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]",
        version_file.read(),
        re.M
    )
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

setup(
    version=version,
    install_requires=[
        # The Python.net team hasn't published 2.X wheels for Python 3.9 or 3.10,
        # and their development effort seems to be focussed on the 3.X branch;
        # they've indicated they're not planning to make the 2.X branch compatible
        # with Python 3.10. If we want to be able to support "current" Python,
        # we need to work off a source release until they formally release 3.0.
        #
        # The most recent version of pythonnet is the alpha version 3.0.0a1.
        # At the moment we will use this version until an official release
        # will be published.
        'pythonnet==3.0.0a1',
        'toga-core==%s' % version,
    ],
    test_suite='tests',
    test_require=[
        'toga-dummy==%s' % version,
    ]
)
