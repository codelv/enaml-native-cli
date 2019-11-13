# -*- coding: utf-8 -*-
import os
import sys
import json
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

# Create the environment
p = conda('env', 'create', '--file', 'environment.yml',
          _bg=True, _err_to_out=True, _out=process, **kw)
p.wait()

# Find the env
data = json.loads(str(conda('env', 'list', '--json')))

# Create a symlink from app/venv folder to the conda env
env_name = '{{ cookiecutter.project_name.lower().replace(" ", "") }}'
for path in data['envs']:
    if os.path.split(path)[-1] == env_name:
        os.symlink(path ,'venv')
        break
if not os.path.exists('venv'):
    print("Could not create a link to the env!")
    sys.exit(1)
