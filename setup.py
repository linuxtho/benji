#!/usr/bin/env python

import os
import sys

import benji


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as file:
    requirements = file.read().splitlines()


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: Internet',
] 


setup(
    name='benji',
    version=benji.VERSION,
    description='IRC Robot',
    license='Apache 2.0',
    url='https://github.com/linuxtho/benji',
    entry_points={
        'console_scripts': [
            'benji = benji.main:main',
        ]
    },
    packages=['benji'],
    install_requirements=requirements,
)
