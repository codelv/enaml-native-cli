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

Start a new enaml-native project. It now uses [cookiecutter](http://cookiecutter.readthedocs.io/) 
and will prompt for any required input.

```bash 

enaml-native create app

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

List apps requirements (or use conda list)

```bash
enaml-native list
```

Build and run your app

```bash

#: Run the app (or build-android) to build
enaml-native run-android

```

To add and remove packages or create new packages see the new cross compiling
toolchain [conda-mobile](https://github.com/codelv/conda-mobile)
 
