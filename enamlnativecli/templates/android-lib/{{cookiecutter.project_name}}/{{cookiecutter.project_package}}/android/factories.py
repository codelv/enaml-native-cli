"""
Copyright (c) 2018, {{cookiecutter.author}}.

Distributed under the terms of the {{cookiecutter.project_license}} License.

The full license is in the file COPYING.txt, distributed with this software.

"""

# Add all the native widgets that you want the android library to expose
# for use in enamlnative.
def {{cookiecutter.widget_module}}_factory():
    from .android_{{cookiecutter.widget_module}} import Android{{cookiecutter.widget_name}}
    return Android{{cookiecutter.widget_name}}


def install():
    from enamlnative.android import factories
    
    # Add your native widgets here with the convention
    factories.ANDROID_FACTORIES.update({
      "{{cookiecutter.widget_name}}": {{cookiecutter.widget_module}}_factory
    })
