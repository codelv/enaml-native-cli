# 2.3.2

- Migrate to androidx support libraries
- When a command requires an apps virtual env to be active show an error if
it's not

# 2.3.1

Add support for using the environment.yml file to manage the dependencies.

> Note: The `venv` folder is now symlink to the conda environment in the default
> location.

To update an app to match the dependencies in the `environment.yml` file simply
run `enaml-native install` without any arguments.

The environment also uses the app name so you can now use
`conda activate <appname>` (all lowercase) instead of `./venv`.

When removing an app you must either use `rm -Rl` to follow the link to the
venv folder or manually remove the env created with
`conda env remote -n <appname>`.


# 2.3.0

- Update gradle to 5.1.1 and tools to 3.4.2

# 2.2.7-2.2.11

- Leave multiprocessing in by default
- Fix building on windows

# 2.2.6

- Show help when no args are given on Python 3

# 2.2.5

- Fix bug where python 3 is trying to use ndk-build on 2.7

# 2.2.4

- Add windows support

# 2.2.2

- Add python 3 support

# 2.2.1

- Add `ndk-stack` command to easily debug crashes in native libs

# 2.0.0

- Move to conda-mobile
- Refactor to use cookiecutter
