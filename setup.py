# -*- coding: utf-8 -*-
"""Installer for this package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

version = '1.0'

long_description = \
    read('docs', 'README.rst') + \
    read('docs', 'CHANGES.rst') + \
    read('docs', 'LICENSE.rst')

setup(
    name='matem.chartkick',
    version=version,
    description="Plone Integration of chartkick plugin",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='Plone Python',
    author='Informática Académica',
    author_email='computoacademico@im.unam.mx',
    url='https://github.com/imatem/matem.chartkick',
    license='BSD',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['matem'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Pillow',
        'Plone',
        'setuptools',
    ],
    extras_require={
        'develop': [
            'flake8',
            'plone.app.debugtoolbar',
            'plone.reload',
            'Products.PDBDebugMode',
            'Products.PrintingMailHost',
            'Sphinx',
            'zptlint',
        ],
        'test': [
            'mock',
            'plone.app.robotframework',
            'plone.app.testing',
            'unittest2',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
