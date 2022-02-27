# -*- coding: utf-8 -*-
import json
import os
import sys

from enamlnativecli.main import find_conda

# Find conda on the system
conda = find_conda()
kw = {}
IS_WIN = "win32" in sys.platform

if IS_WIN:
    process = sys.stdout
else:
    kw["_out_bufsize"] = 0

    def process(c):
        sys.stdout.write(c)
        sys.stdout.flush()


# Create the environment
p = conda(
    "env",
    "create",
    "--file",
    "environment.yml",
    _bg=True,
    _err_to_out=True,
    _out=process,
    **kw
)
p.wait()

# Find the env
output = conda("env", "list", "--json")
data = json.loads(str(output.stdout if IS_WIN else output))

# Create a symlink from app/venv folder to the conda env
env_name = "{{ cookiecutter.project_name.lower().replace(" ", "") }}"
for path in data["envs"]:
    if os.path.split(path)[-1] == env_name:
        os.symlink(path, "venv")
        break
if not os.path.exists("venv"):
    print(f"WARNING: Could not create a link to the env '{env_name}'!")
