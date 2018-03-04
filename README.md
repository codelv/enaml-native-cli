# enaml-native-cli

[![Build Status](https://travis-ci.org/codelv/enaml-native-cli.svg?branch=master)](https://travis-ci.org/codelv/enaml-native-cli)

Cli for [enaml-native](https://github.com/codelv/enaml-native). This is for the new build 
system which allows more modular app builds.
 
This is used to:
 
 1. create new apps
 2. install and remove app packages and dependencies
 3. build and run your apps 

Now uses [conda-mobile](https://github.com/codelv/conda-mobile) for managing app 
dependencies and works same for iOS and Android. Android apps can also be built 
on windows!
 
 
### Installation

Install via pip using the `--user` flag. 

```bash 

#: Do either
pip install --user enaml-native-cli


```


### Usage

Start a new enaml-native project:`

```bash 

enaml-native create app <AppName>

```

It will prompt you for different configuration variables. Most can be left
as is but at a minimum the `app_name` and `bundle_id` should be changed.

Once done, cd to the app folder (the project name) and activate the app's 
environment.

```bash 
cd HelloWorld

# on OSX / linux
source activate ./venv

# on windows simply do
activty venv

```

Now install any app requirements (or use `pip install` and `enaml-native link`)

```bash

enaml-native install enaml-native-icons

```

List apps requirements (or use pip list)

```bash
enaml-native list
```

Build and run your app

```bash

#: Build python requirements
enaml-native build-python # Build python

#: Run the app (or build-android) to build
enaml-native run-android

```



### Creating an Enaml Package

The `enaml-native-cli` was designed to be as configurable as 
possible without over complicating the code. A package is simply a regular
python package that typically includes android and ios resources as `data_files`.

Enaml packages are customizable using setuptool's `entry_points`. The following
entry points are supported:

1. `p4a_recipe` - Entry point that installs a python-for-android recipe. See the p4a docs for examples.
2. `enaml_native_post_install` - Entry point that defines a function that is called when a user runs `enaml-native install <your-package>`
3. `enaml_native_linker` - Entry point that defines a function that is called to link your package to the user's android and ios projects.
4. `enaml_native_unlinker` - Entry point that defines a function that is called to unlink your package from the user's android and ios projects.
5. `enaml_native_pre_uninstall` - Entry point that defines a function that is called when a user runs `enaml-native uninstall <your-package>`

All of these are optional. Search the `enaml-native` script commands for where exactly they are called.


### Adding commands to the CLI

Commands can be added by using the `enaml_native_command` entry point. 

The entry point must return a subclass (NOT an instance) of the `Command` class. 

This command will be added to the cli and can be accessed from the context (via `ctx.cmds['cmd-name']`) 
whenever your package is installed.
 
