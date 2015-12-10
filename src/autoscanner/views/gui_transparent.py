"""
Created on 22 nov. 2015

@author: Valtyr Farshield
"""

import sys
from PySide import QtGui, QtCore
from autoscanner.tools.scantools import ScanTools


class TransparentWindow(QtGui.QDialog):
    """
    Full-screen transparent window used for defining a capture zone
    """
    OPACITY = 0.25

    def __init__(self, parent=None):
        super(TransparentWindow, self).__init__(parent)

        self.layout = QtGui.QGridLayout()
        self.setLayout(self.layout)

        self.setWindowOpacity(TransparentWindow.OPACITY)
        self.showMaximized()
        self.activateWindow()
        self.raise_()
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)

        self.origin = None
        screen_geometry = ScanTools.get_full_screen_geometry()
        self.setGeometry(screen_geometry)
        self.rubber_band = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.rubber_band.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
        self.rubber_band.show()

    def mouseMoveEvent(self, event):
        self.rubber_band.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized())

    def mouseReleaseEvent(self, event):
        self.rubber_band.hide()
        self.accept()


def main():
    QtGui.QApplication(sys.argv)
    trans_window = TransparentWindow()

    if trans_window.exec_():
        print trans_window.rubber_band.geometry()
    else:
        print "Closed"

if __name__ == '__main__':
    main()
