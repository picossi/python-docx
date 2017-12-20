#!/usr/bin/env python

import os
import re

from setuptools import find_packages, setup


def text_of(relpath):
    """
    Return string containing the contents of the file at *relpath* relative to
    this file.
    """
    thisdir = os.path.dirname(__file__)
    file_path = os.path.join(thisdir, os.path.normpath(relpath))
    with open(file_path) as f:
        text = f.read()
    return text

# Read the version from docx.__version__ without importing the package
# (and thus attempting to import packages it depends on that may not be
# installed yet)
version = re.search(
    "__version__ = '([^']+)'", text_of('docx/__init__.py')
).group(1)


NAME = 'python-docx-header-footer'
VERSION = version
DESCRIPTION = 'Work with Microsoft Word .docx files. Fork of the https://github.com/python-openxml/python-docx'
KEYWORDS = 'docx office openxml word'
AUTHOR = 'Vinicius Picossi Teruel'
AUTHOR_EMAIL = 'viniciuspicossi@gmail.com'
URL = 'https://github.com/picossi/python-docx'
DOWNLOAD_URL = 'https://github.com/picossi/python-docx/archive/v0.8.7.tar.gz'
LICENSE = text_of('LICENSE')
PACKAGES = find_packages(exclude=['tests', 'tests.*'])
PACKAGE_DATA = {'docx': ['templates/*']}

INSTALL_REQUIRES = ['lxml>=2.3.2']
TEST_SUITE = 'tests'
TESTS_REQUIRE = ['behave', 'mock', 'pyparsing', 'pytest']

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Office/Business :: Office Suites',
    'Topic :: Software Development :: Libraries'
]

LONG_DESCRIPTION = text_of('README.rst') + '\n\n' + text_of('HISTORY.rst')


params = {
    'name':             NAME,
    'version':          VERSION,
    'description':      DESCRIPTION,
    'keywords':         KEYWORDS,
    'long_description': LONG_DESCRIPTION,
    'author':           AUTHOR,
    'author_email':     AUTHOR_EMAIL,
    'url':              URL,
    'download_url':     DOWNLOAD_URL,
    'license':          LICENSE,
    'packages':         PACKAGES,
    'package_data':     PACKAGE_DATA,
    'install_requires': INSTALL_REQUIRES,
    'tests_require':    TESTS_REQUIRE,
    'test_suite':       TEST_SUITE,
    'classifiers':      CLASSIFIERS,
}

setup(**params)
