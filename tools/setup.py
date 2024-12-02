#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Best practices for setup.py and requirements.txt
https://caremad.io/posts/2013/07/setup-vs-requirement/
"""

from setuptools import setup, find_packages

setup(
    name='schema-registry-tools',
    version='0.0.1', 
    description='Schema Registry API and CLI commands',
    author='Provenant',
    url='https://github.com/provenant-dev/public-schema',
    python_requires='>=3.10.4',
    packages=find_packages(include=['cli', 'api', 'cli.*', 'api.*']),
    install_requires=[
        'keri @ git+https://github.com/provenant-dev/keripy.git@pr-main'
    ],    
    entry_points={
        'console_scripts': [
            'schema_registry_server = api.server:main',
            'saidify_schema = cli.saidify_schema:main',
            'saidify_sad = cli.saidify_sad:main',
            'register_all = cli.register_all:main'
        ]
    }
)