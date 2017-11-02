"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 31, 2017

@author: jrm
"""
import os
import sh

from pythonforandroid.logger import shprint


def test_init():
    cmd = sh.Command('enaml-native')
    shprint(cmd, 'init', 'HelloWorld', 'com.example.helloworld', 'tmp/',
            '--dev-cli', '.', _debug=True)

    #: Try to build
    os.chdir('tmp/HelloWorld/')
    shprint(sh.bash, '-c',
           'source venv/bin/activate && enaml-native build-python', _debug=True)


def test_init_package():
    cmd = sh.Command('enaml-native')
    shprint(cmd, 'init-package', 'enaml-native-test', 'tmp/', _debug=True)