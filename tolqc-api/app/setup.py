# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

# coding: utf-8

from setuptools import find_packages, setup

NAME = 'tolqc-api'
VERSION = '1.1.2'
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description='Tree of Life QC API',
    author_email='tol-platforms@sanger.ac.uk',
    url='',
    keywords=['Swagger', 'Tree of Life QC API'],
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['app=main.run:main']},
    long_description="""\
    API for ToLQC
    """
)
