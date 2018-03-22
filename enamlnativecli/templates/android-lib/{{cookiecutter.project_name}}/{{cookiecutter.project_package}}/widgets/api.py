"""
Copyright (c) 2018, {{cookiecutter.author}}.

Distributed under the terms of the {{cookiecutter.project_license}} License.

The full license is in the file COPYING.txt, distributed with this software.

"""
# Import any other widgets here
from .{{cookiecutter.widget_module}} import {{cookiecutter.widget_name}}


def install():
    from enamlnative.widgets import api

    # Add any other widgets here
    setattr(api, '{{cookiecutter.widget_name}}', {{cookiecutter.widget_name}})
