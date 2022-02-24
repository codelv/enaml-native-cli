"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the GPLv3 License.

The full license is in the file COPYING.txt, distributed with this software.

Created on July 10, 2017

@author: jrm
"""
import re
import os
from setuptools import setup, find_packages


def find_data(folder):
    """Include everything in the folder"""
    for (path, directories, filenames) in os.walk(folder):
        for filename in filenames:
            yield os.path.join("..", path, filename)


def find_version():
    with open(os.path.join("enamlnativecli", "__init__.py")) as f:
        for line in f:
            m = re.search(r'version = [\'"](.+)[\'"]', line)
            if m:
                return m.group(1)
    raise Exception("Couldn't find the version number")


setup(
    name="enaml-native-cli",
    version=find_version(),
    author="CodeLV",
    author_email="info@codelv.com",
    license="GPLv3",
    url="https://codelv.com/projects//enaml-native",
    description="Build native mobile apps in python",
    entry_points={"console_scripts": ["enaml-native = enamlnativecli.main:main"]},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    package_data={"": list(find_data("enamlnativecli"))},
    include_package_data=True,
    install_requires=["sh", "atom", "ruamel.yaml", "cookiecutter", "pbs"],
    test_requires=["requests", "py.test", "pytest-cov", "pytest-timeout"],
)
