"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 31, 2017

@author: jrm
"""
import json
import os
from contextlib import contextmanager

import sh
from pythonforandroid.logger import shprint
from pythonforandroid.util import current_directory


@contextmanager
def source_activated(venv, command):
    print(f"[DEBUG]: Activating {venv} for command {command}")

    def cmd(*args, **kwargs):
        #: Make a wrapper to a that runs it in the venv
        return sh.bash(
            "-c",
            f"source {venv}/bin/activate && {cmd} {' '.join(args)}",
            **kwargs,
        )

    yield cmd

    print(f"[DEBUG]: Deactivating {venv} for {command}")


@contextmanager
def app_config(path="package.json"):
    with open(path) as f:
        config = json.load(f)

    yield config

    #: Save changes
    with open("package.json", "w") as f:
        json.dump(config, f)


def test_crystax():
    if os.path.exists("tmp/TestCrystax"):
        sh.rm("-R", "tmp/TestCrystax")
    cmd = sh.Command("enaml-native")
    shprint(
        cmd,
        "init",
        "TestCrystax",
        "com.codelv.testcrystax",
        "tmp/",
        "--dev-cli",
        ".",
        _debug=True,
    )

    #: Try to build
    with current_directory("tmp/TestCrystax/"):

        #: Update the sdk/ndk paths
        if "TRAVIS" in os.environ:
            with app_config("package.json") as config:
                # config['android']['ndk'] = '~/Android/Crystax/crystax-ndk-10.3.2/'
                config["android"]["sdk"] = "/usr/local/android-sdk/"

        #: Now activate venv and build
        with source_activated("venv", "enaml-native") as cmd:
            shprint(cmd, "build-python", _debug=True)
            shprint(cmd, "run-android", _debug=True)


# def test_python2():
#     if os.path.exists('tmp/TestPython2'):
#         sh.rm('-R', 'tmp/TestPython2')
#     cmd = sh.Command('enaml-native')
#     shprint(cmd, 'init', 'TestPython2', 'com.codelv.testpython2', 'tmp/',
#             '--dev-cli', '.', _debug=True)
#
#     #: Try to build
#     with current_directory('tmp/TestPython2/'):
#
#         #: Update the sdk/ndk paths
#         if 'TRAVIS' in os.environ:
#             with app_config('package.json') as config:
#                 config['android']['ndk'] = '/usr/local/android-sdk/ndk-bundle/'
#                 config['android']['sdk'] = '/usr/local/android-sdk/'
#
#         #: Now activate venv and build
#         with source_activated('venv', 'enaml-native') as cmd:
#             #: Install p4a-python2
#             shprint(cmd, 'install', 'p4a-python2==2.7.13r4', _debug=True)
#
#             #: Update package to use python2 instead of python2crystax
#             with app_config('package.json') as config:
#
#                 #: Update NDK
#                 config['android']['ndk'] = os.path.join(config['android']['sdk'], 'ndk-bundle')
#
#                 #: Remove crystax and add python2
#                 del config['android']['dependencies']['python2crystax']
#                 config['android']['dependencies']['python2'] = ""  # It uses the recipe version
#
#                 #: Ctx manager saves it
#
#             #: Now build
#             shprint(cmd, 'build-python', _debug=True)
#
#             #: And run
#             # TODO: shprint(cmd, 'run-android', _debug=True)


def test_init_package():
    if os.path.exists("tmp/enaml-native-test"):
        sh.rm("-R", "tmp/enaml-native-test")
    cmd = sh.Command("enaml-native")
    shprint(cmd, "init-package", "enaml-native-test", "tmp/", _debug=True)
