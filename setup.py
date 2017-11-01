"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on July 10, 2017

@author: jrm
"""
import os
import fnmatch
from setuptools import setup


def find_data_files(dest, *folders):
    matches = {}
    #: Want to install outside the venv volder in the packages folder
    dest = os.path.join('packages', dest)

    excluded_types = ['.pyc', '.enamlc', '.apk', '.iml','.zip', '.tar.gz', '.so', '.gif', '.svg']
    excluded_dirs = ['android/build', 'android/captures', 'android/assets',
                     'python-for-android/doc', 'bootstraps/pygame', 'python-for-android/testapps',
                     'python-for-ios/tools/external']
    for folder in folders:
        if not os.path.isdir(folder):
            k = os.path.join(dest, dirpath)
            matches[k].append(os.path.join(dest,folder))
            continue
        for dirpath, dirnames, files in os.walk(folder):
            #: Skip build folders and exclude hidden dirs
            if ([d for d in dirpath.split("/") if d.startswith(".")] or
                    [excluded_dir for excluded_dir in excluded_dirs if excluded_dir in dirpath]):
                continue
            k = os.path.join(dest, dirpath)
            if k not in matches:
                matches[k] = []
            for f in fnmatch.filter(files, '*'):
                if [p for p in excluded_types if f.endswith(p)]:
                    continue
                m = os.path.join(dirpath, f)
                matches[k].append(m)
    return matches.items()


setup(
    name="enaml-native-cli",
    version="1.2",
    author="CodeLV",
    author_email="frmdstryr@gmail.com",
    license='MIT',
    url='https://github.com/codelv/enaml-native-cli/',
    description="Build native mobile apps in python",
    scripts=['enaml-native'],
    long_description=open("README.md").read(),
    data_files=find_data_files('enaml-native-cli', 'android', 'ios',
                               'python-for-android', 'python-for-ios'),
    install_requires=[
        'appdirs', 'colorama>=0.3.3', 'sh>=1.10,<1.12.5', 'jinja2', 'six', 'pipdeptree',
        'atom', 'ply',
    ],
    setup_requires=['virtualenv'],
    test_requires=['requests', 'py.test', 'pytest-cov', 'pytest-catchlog', 'pytest-timeout']
)
