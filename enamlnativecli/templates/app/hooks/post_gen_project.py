# -*- coding: utf-8 -*-
import sh
import sys


def process(line):
    sys.stdout.write(line)
    sys.stdout.flush()


p = sh.conda('create', '-p', 'venv', '-c', 'codelv', '--use-local', '--yes',
             'python={{cookiecutter.python_version}}',
             'enaml-native', _bg=True, _err_to_out=True, _out=process)
p.wait()
