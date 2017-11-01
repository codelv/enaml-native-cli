"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 31, 2017

@author: jrm
"""
import os
import sh


def test_init():
    cmd = sh.Command('enaml-native')
    cmd('init', 'HelloWorld', 'com.example.helloworld', 'tmp/')

    #: Try to build
    os.chdir('tmp/HelloWorld')
    sh.bash('-c', 'source venv/bin/activate && enaml-native build-python')
