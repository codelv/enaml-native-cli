"""
Copyright (c) 2018, {{cookiecutter.author}}.

Distributed under the terms of the {{cookiecutter.project_license}} License.

The full license is in the file COPYING.txt, distributed with this software.

"""
from atom.api import Typed, Instance, Dict, Bool, set_default

from {{cookiecutter.project_package}}.widgets.{{cookiecutter.widget_module}} import (
    Proxy{{cookiecutter.widget_name}}
)
from enamlnative.core import bridge
#from enamlnative.android.android_toolkit_object import AndroidToolkitObject
from enamlnative.android.android_view import AndroidView
from enamlnative.android.bridge import (
    JavaBridgeObject, JavaMethod, JavaStaticMethod, JavaCallback, JavaProxy
)


class {{cookiecutter.widget_name}}(AndroidView):
    __nativeclass__ = set_default(
        '{{cookiecutter.bundle_id}}.{{cookiecutter.widget_name}}')

    # Add any JavaMethod, JavaCallbacks, etc.. that you want the native widget
    # to expose to be used in enaml-native.
    # setValue = JavaMethod('java.lang.String')

class Android{{cookiecutter.widget_name}}(AndroidView, Proxy{{cookiecutter.widget_name}}):
    """ An Android implementation of an Enaml Proxy{{cookiecutter.widget_name}}.

    """

    #: Holder
    widget = Typed({{cookiecutter.widget_name}})

    # -------------------------------------------------------------------------
    # Initialization API
    # -------------------------------------------------------------------------
    def create_widget(self):
        """ Create the underlying widget.

        """
        self.widget = {{cookiecutter.widget_name}}(self.get_context())


    def init_widget(self):
        """ Initialize the widget state. By default enamlnative will invoke
        set_<property> on any attribute defined in the enamldef block.
        
        """
        super(Android{{cookiecutter.widget_name}}, self).init_widget()

    # -------------------------------------------------------------------------
    # Proxy{{cookiecutter.widget_name}} API
    # -------------------------------------------------------------------------

    # Add any handlers here that will update the native widget when the
    # enaml declaration changes. These are called by the _update_proxy method
    # when any observed values are changed.
    #def set_value(self, value):
    #    # This sets the value over the bridge
    #    self.widget.setValue(value)