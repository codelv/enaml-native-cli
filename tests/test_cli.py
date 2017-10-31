"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 31, 2017

@author: jrm
"""
import sh

def test_init():
    cmd = sh.Command('enaml-native')
    cmd('init', 'HelloWorld', 'com.example.helloworld', 'tmp/')
