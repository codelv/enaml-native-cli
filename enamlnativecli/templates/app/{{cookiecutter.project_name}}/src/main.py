import sys

import enaml


def get_application():
    if sys.platform == "darwin":
        from enamlnative.ios.app import IPhoneApplication

        return IPhoneApplication
    else:
        from enamlnative.android.app import AndroidApplication

        return AndroidApplication


def main():
    with enaml.imports():
        from activity import MainActivity

    Application = get_application()
    app = Application(
        debug=False,  # Uncomment to debug the bridge
        dev="",  # Set to 'server', 'remote', an IP address
        activity=MainActivity(),
    )
    app.start()


if __name__ == "__main__":
    # This is used when remote debugging
    # Init remote nativehooks implementation
    from enamlnative.core import remotehooks

    remotehooks.init()
    main()
