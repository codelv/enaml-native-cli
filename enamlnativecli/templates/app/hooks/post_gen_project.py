# -*- coding: utf-8 -*-
import sys

kw = {}

# sh does not work on windows
if 'win' in sys.platform:
    import pbs
    import os
    from os.path import join, exists

    class Sh(object):
        def __getattr__(self, attr):
            if hasattr(pbs, attr):
                return getattr(pbs, attr)
            return pbs.Command(attr)
    sh = Sh()
    miniconda2 = join(os.getenv('PROGRAMDATA'),'miniconda2','scripts','conda.exe')
    miniconda3 = join(os.getenv('PROGRAMDATA'),'miniconda3','scripts','conda.exe')
    if exists(miniconda2):
        sh.conda = sh.Command(miniconda2)
    if exists(miniconda3):
        sh.conda = sh.Command(miniconda3)
    process = sys.stdout

else:
    import sh
    kw['_out_bufsize'] = 0

    def process(c):
        sys.stdout.write(c)
        sys.stdout.flush()


p = sh.conda('create', '-p', 'venv', '-c', 'codelv', '--use-local', '--yes',
             'python={{cookiecutter.python_version}}',
             'enaml-native', _bg=True, _err_to_out=True, _out=process, **kw)
p.wait()
