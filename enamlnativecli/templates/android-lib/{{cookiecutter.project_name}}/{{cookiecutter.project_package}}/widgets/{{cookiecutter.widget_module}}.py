"""
Copyright (c) 2018, {{cookiecutter.author}}.

Distributed under the terms of the {{cookiecutter.project_license}} License.

The full license is in the file COPYING.txt, distributed with this software.

"""
from atom.api import Typed, ForwardTyped, set_default, observe
from enaml.core.declarative import d_

# Use these if your widget subclasses java.lang.Object
# from enaml.widgets.toolkit_object import ToolkitObject, ProxyToolkitObject

# Use these if your widget subclasses android.view.View
from enamlnative.widget.view import View, ProxyView


class Proxy{{cookiecutter.widget_name}}(ProxyView):
    """ The abstract definition of a proxy {{cookiecutter.widget_name}} object.

    """
    #: A reference to the declaration.
    declaration = ForwardTyped(lambda: {{cookiecutter.widget_name}})

    #: Replace this with your properties
    #def set_value(self, name):
    #    raise NotImplementedError


class {{cookiecutter.widget_name}}(View):
    """ Declaration for a {{cookiecutter.widget_name}}. This defines
    the api that is used within enaml files.

    """

    #: Add your properties here
    #value = d_(Unicode())

    #: A reference to the Proxy{{cookiecutter.widget_name}} object.
    proxy = Typed(Proxy{{cookiecutter.widget_name}})

    #@observe('value')
    #def _update_proxy(self, change):
    #    """ An observer which sends the state change to the proxy.
    #    This updates the proxy widget whenever the declaration changes.
    #
    #    """
    #    # The superclass implementation is sufficient.
    #    super({{cookiecutter.widget_name}}, self)._update_proxy(change)
