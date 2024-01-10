#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Best practices for setup.py and requirements.txt
https://caremad.io/posts/2013/07/setup-vs-requirement/
"""

from setuptools import setup

setup(
    name='schema-cli',
    version='0.0.1', 
    description='CLI commands',
    author='Provenant',
    url='https://github.com/provenant-dev/public-schema',
    python_requires='>=3.10.4',
    install_requires=[
        'keri @ git+https://git@github.com/WebOfTrust/keripy.git'         
    ],    
    entry_points={
        'console_scripts': [
            'saidify-schema = cli.saidify:main'
        ]
    }
)