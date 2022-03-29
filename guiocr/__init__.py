# -*- coding:utf-8 -*-
import logging
import sys

from PyQt5.Qt import PYQT_VERSION_STR as QT_VERSION
__appname__="文本识别检测"

__version__ = "1.1"


QT4 = QT_VERSION[0] == "4"
QT5 = QT_VERSION[0] == "5"
del QT_VERSION

PY2 = sys.version[0] == "2"
PY3 = sys.version[0] == "3"
del sys
