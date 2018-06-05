# -*- coding: utf-8 -*-
import sys
from enamlnativecli.main import find_conda

# Find conda on the system
conda = find_conda()
kw = {}

if 'win' in sys.platform:
    process = sys.stdout
else:
    kw['_out_bufsize'] = 0

    def process(c):
        sys.stdout.write(c)
        sys.stdout.flush()


p = conda('create', '-p', 'venv', '-c', 'codelv', '--use-local', '--yes',
          'python={{cookiecutter.python_version}}', 'enaml-native', _bg=True,
          _err_to_out=True, _out=process, **kw)
p.wait()
