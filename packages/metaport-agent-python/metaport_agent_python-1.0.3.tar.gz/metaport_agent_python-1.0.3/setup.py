#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Setup script for Metaport Python Agent.

This script provides pip installation support for the Metaport agent,
ensuring compatibility with Python 3.9+ environments.
"""

from setuptools import setup, find_packages
import os

# Read version from __init__.py
def get_version():
    """Extract version from package __init__.py file."""
    init_path = os.path.join(os.path.dirname(__file__), 'metaport', '__init__.py')
    with open(init_path, 'r') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.split('=')[1].strip().strip('"\'')
    return '1.0.0'

# Read README for long description
def get_long_description():
    """Read README.md for package description."""
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return "Metaport Python Agent for SBOM generation and reporting"

setup(
    name='metaport-agent-python',
    version=get_version(),
    description='Python agent for Metaport SBOM generation and reporting',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Metaport Team',
    author_email='support@metaport.com',
    url='https://getmetaport.com',
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.9',
    install_requires=[
        'requests>=2.20.0',     # For HTTPS transport, Python 3.9+ compatible
        'toml>=0.10.0',         # For Poetry pyproject.toml parsing, Python 3.9+ compatible
        'PyNaCl>=1.4.0',        # For email attachment encryption (libsodium), Python 3.9+ compatible
        'cyclonedx-bom>=3.0.0', # For SBOM generation, Python 3.9+ compatible
        'ko-poetry-audit-plugin>=0.2.0',  # For vulnerability scanning, requires Python 3.9+
    ],
    extras_require={
        'dev': [
            'pytest>=3.6.0',
            'pytest-cov>=2.6.0',
            'flake8>=3.5.0',
            'black>=18.9b0; python_version>="3.6"',  # Black requires Python 3.6+
        ]
    },
    entry_points={
        'console_scripts': [
            'metaport-agent=metaport.metaport:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',

        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Systems Administration',
        'Topic :: Security',
    ],
    keywords='metaport sbom security dependencies vulnerability scanning',
    project_urls={
        'Homepage': 'https://getmetaport.com',
        'Documentation': 'https://getmetaport.com/docs',
        'Source': 'https://gitlab.com/dcentrica/metaport/metaport-agent-python',
        'Tracker': 'https://gitlab.com/dcentrica/metaport/metaport-agent-python/-/issues',
    },
)