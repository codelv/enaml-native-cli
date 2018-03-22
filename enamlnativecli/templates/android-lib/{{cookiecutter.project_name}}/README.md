# {{cookiecutter.project_name}}

A {{cookiecutter.widget_name}} for enaml-native.

### Overview

This template creates all the boilerplate for adding a native widget to your enaml-native apps 
as an installable conda package. The idea is to have an easy way for users to install and use
native android libraries and widgets without needing to know java/gradle, etc..

The template creates the following:

1. An android library in the `android` folder
2. A python package to use the android library in the `src` folder
3. A conda recipe (`build.sh` and `meta.yaml`) 

These are decribed below.

###### Android library

When this package is installed into a users app environment, the enaml-native cli will "link" this 
library and the included Package.java to the users app.

Linking simply adds the library to the users `app/build.gradle` and adds the included Package.java
file to the list of packages used in their main activity. This is very similar to how react-native 
does it. 

The package at `android/src/main/java/{{cookiecutter.bundle_path}}/{{cookiecutter.project_name}}Package.java` 
is your hook into the users app.  This Package lets your library add "packers" and "unpackers" into 
the bridge so it knows how to encode and decode any special data types your native libraries provide 
(ex converting SensorData to a dict). It also receives lifecycle events from the app's main activity 
so you can handle them if your library needs.

Use `android/src/main/build.gradle` to include any gradle dependencies your library needs. 
This is often this is the only file you need to modify to include an existing library.

Use `android/src/main/AndroidManifext.xml` to add any permissions, etc.. your library needs.

###### Python package

The generated python package in the `src` folder contains two subpackages `widgets` and `android`.

The `widgets` package contains the enaml declaration that defines what properites, callbacks,
etc.. users can use within their apps enaml UI files. It also contains an `api` module that users
can use to import all of your native widgets from.
 
```python

#: How users can import your new native widget
from {{cookiecutter.project_package}}.widgets.api import {{cookiecutter.widget_name}}
 
```

Alternatively they can invoke `install()` which will add these to the `enamlnative.widgets.api` module.

The `android` package contains the implementation of that declaration. You will need to expose
any methods/callbacks/objects your widgets use using a JavaBridgeObject wrapper that allows python
to access or "proxy" the real native object over the bridge.  See the implementation of all the
widgets in the core enaml-native package for examples of how to do this.


###### Conda recipe

The `build.sh` and `meta.yaml` are files needed to package the library as a conda recipe. 
 
The builds script, `build.sh`, simply copies the `src` folder to the site-packages for each 
supported android abi (arm, arm64, x86, x86_64). Then copies and renames the `android` folder
into the users environment to `<env-root>/android/{{cookiecutter.project_name}}}}`

You can build this recipe using `conda-build .` from within this folder. Once built it's ready to be  
installed and used.

### Installing

Install `{{cookiecutter.project_name}}` using the [enaml-native-cli](https://github.com/codelv/enaml-native-cli) (or conda)

```bash

#: Using the enaml-native cli
enaml-native install {{cookiecutter.project_name}}

```

Then add `{{cookiecutter.project_name}}""` to your app's `environment.yaml`




