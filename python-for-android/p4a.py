# -*- coding: utf-8 -*-
import os

if 'TRAVIS' in os.environ:
    #: Force UTF8 encoding
    import sys
    # sys.setdefaultencoding() does not exist, here!
    reload(sys)  # Reload does the trick!
    sys.setdefaultencoding('UTF8')

from pythonforandroid.toolchain import main

if __name__=='__main__':
    main()
