#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='swagger_ui',
    version='2.2.5',
    description="The Swagger UI resources as a Python Package.",
    long_description=readme + '\n\n' + history,
    author="Rafael Caricio",
    author_email='rafael@caricio.com',
    url='https://github.com/rafaelcaricio/swagger_ui',
    packages=[
        'swagger_ui',
    ],
    package_dir={'swagger_ui':
                 'swagger_ui'},
    entry_points={
        'console_scripts': [
            'swagger_ui=swagger_ui.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='swagger_ui',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
