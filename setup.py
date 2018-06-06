"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the GPLv3 License.

The full license is in the file COPYING.txt, distributed with this software.

Created on July 10, 2017

@author: jrm
"""
import os
from setuptools import setup, find_packages


def find_data(folder):
    """ Include everything in the folder """
    for (path, directories, filenames) in os.walk(folder):
        for filename in filenames:
            yield os.path.join('..', path, filename)


setup(
    name="enaml-native-cli",
    version="2.2.11",
    author="CodeLV",
    author_email="frmdstryr@gmail.com",
    license='GPLv3',
    url='https://github.com/codelv/enaml-native-cli/',
    description="Build native mobile apps in python",
    entry_points={'console_scripts': [
        'enaml-native = enamlnativecli.main:main']},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={'': find_data('enamlnativecli')},
    include_package_data=True,
    install_requires=['sh', 'atom', 'ruamel.yaml', 'cookiecutter', 'pbs'],
    test_requires=['requests', 'py.test', 'pytest-cov', 'pytest-timeout']
)
