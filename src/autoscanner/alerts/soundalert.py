"""
Created on 29 nov. 2015

@author: Valtyr Farshield
"""

import sys
import time
import winsound
from PySide import QtGui, QtCore


class SoundAlert(QtCore.QObject):
    """
    Acoustic warning system
    """

    FREQ = 400       # Hz
    TIME_ON = 250    # milliseconds
    TIME_OFF = 3000  # milliseconds

    finished = QtCore.Signal()

    def __init__(self, parent=None):
        super(SoundAlert, self).__init__(parent)

        self.exiting = False

    def process(self):
        seconds_to_sleep = SoundAlert.TIME_OFF / 1000

        while not self.exiting:
            counter = seconds_to_sleep / 0.1

            while not self.exiting and counter > 0:
                time.sleep(0.1)
                counter -= 1

            if not self.exiting:
                winsound.Beep(SoundAlert.FREQ, SoundAlert.TIME_ON)

        self.finished.emit()


def main():

    class Form(QtGui.QDialog):
        def __init__(self, parent=None):
            super(Form, self).__init__(parent)

            # GUI setup
            layout = QtGui.QHBoxLayout()
            btn1 = QtGui.QPushButton("Alarm")
            btn1.clicked.connect(self.alarm_start)
            layout.addWidget(btn1)
            self.setLayout(layout)

            # Thread config
            self.worker_thread = QtCore.QThread()
            self.red_alert = SoundAlert()
            self.red_alert.moveToThread(self.worker_thread)
            self.red_alert.finished.connect(self.worker_thread.quit)
            self.worker_thread.started.connect(self.red_alert.process)

        @QtCore.Slot()
        def alarm_start(self):
            self.red_alert.exiting = False
            self.worker_thread.start()

            QtGui.QMessageBox.information(self, "test", "test")
            self.red_alert.exiting = True

    app = QtGui.QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
