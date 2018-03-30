# -*- coding: utf-8 -*-
import sh
import sys


def process(line):
    sys.stdout.write(line)
    sys.stdout.flush()


p = sh.conda('create', '-p', 'venv', '-c', 'codelv', '--use-local', '--yes',
             'enaml-native', _bg=True, _err_to_out=True, _out=process)
p.wait()
