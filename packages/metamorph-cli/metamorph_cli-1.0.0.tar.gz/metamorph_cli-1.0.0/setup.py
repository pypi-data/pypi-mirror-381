#!/usr/bin/env python3
"""Setup script for MetaMorph."""

from setuptools import setup
import os

# Read the README file
def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

setup(
    name='metamorph-cli',
    version='1.0.0',
    description='Transform your file metadata with ease',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Atrid Ahmetaj',
    author_email='',
    url='https://github.com/atridahmetaj/metamorph',
    py_modules=['metamorph'],
    install_requires=[
        'PyPDF2>=3.0.0',
        'Pillow>=10.0.0',
        'mutagen>=1.47.0',
    ],
    entry_points={
        'console_scripts': [
            'metamorph=metamorph:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Operating System :: OS Independent',
        'Environment :: Console',
    ],
    python_requires='>=3.7',
    keywords='metadata pdf exif audio tags cli',
)
