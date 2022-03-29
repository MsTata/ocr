import argparse
import codecs
import logging
import os
import os.path as osp
import sys
from guiocr import __appname__
from guiocr.app import MainWindow
from guiocr.utils import newIcon
from PyQt5 import QtCore, QtGui, QtWidgets


def main():
    QtCore.QCoreApplication.setOrganizationDomain("casia")
    QtCore.QCoreApplication.setApplicationName(__appname__)
    app = QtWidgets.QApplication(sys.argv)
    app.setApplicationName(__appname__)
    win = MainWindow()

    win.show()
    win.raise_()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

