"""
Copyright (c) 2017, Jairus Martin.

Distributed under the terms of the MIT License.

The full license is in the file COPYING.txt, distributed with this software.

Created on Oct 31, 2017
"""
import os
from contextlib import contextmanager

import pytest

from enamlnativecli.main import cd, sh, shprint


@contextmanager
def source_activated(venv, command):
    print(f"[DEBUG]: Activating {venv} for command {command}")

    def cmd(*args, **kwargs):
        #: Make a wrapper to a that runs it in the venv
        return sh.bash(
            "-c",
            f"source activate {venv} && {command} {' '.join(args)}",
            **kwargs,
        )

    yield cmd

    print(f"[DEBUG]: Deactivating {venv} for {command}")


def test_help(capsys):
    cmd = sh.Command("enaml-native")
    shprint(cmd, "-h", _debug=True)
    cap = capsys.readouterr()
    assert "positional arguments" in cap.out


def test_check_venv_active(capsys):
    cmd = sh.Command("enaml-native")
    with pytest.raises(Exception):
        shprint(cmd, "list", _debug=True)
    cap = capsys.readouterr()
    assert "must be run with an app's env activated" in cap.out


def test_create_app(capsys):
    if not os.path.exists("tmp"):
        os.makedirs("tmp")
    with cd("tmp"):
        if os.path.exists("HelloWorld"):
            sh.rm("-r", "HelloWorld")

        conda = sh.Command("conda")
        # Remove existing env if it exists
        shprint(conda, "env", "remove", "-n", "helloworld")

        cmd = sh.Command("enaml-native")
        shprint(cmd, "create", "app", "--no-input", _debug=True)

        assert os.path.exists("HelloWorld")
        cap = capsys.readouterr()
        assert "App created successfully" in cap.out


def test_build_app(capsys):
    with cd("tmp/HelloWorld"):
        with source_activated("helloworld", "enaml-native") as cmd:
            shprint(cmd, "build-android", _debug=True)


# def test_create_lib():
#    if os.path.exists("tmp/enaml-native-test"):
#        sh.rm("-R", "tmp/enaml-native-test")
#    cmd = sh.Command("enaml-native")
#    shprint(cmd, "init-package", "enaml-native-test", "tmp/", _debug=True)
