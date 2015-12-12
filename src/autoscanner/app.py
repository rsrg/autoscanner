"""
Created on 22 nov. 2015

@author: Valtyr Farshield
"""

import sys
import time
from PySide import QtGui, QtCore

from autoscanner import __organization__, __appname__, __version__
from autoscanner.views.gui_main import Ui_MainWindow
from autoscanner.views.gui_transparent import TransparentWindow
from autoscanner.tools.scantools import ScanTools
from autoscanner.tools.imageprocessor import ImageProcessor
from autoscanner.alerts.soundalert import SoundAlert
from autoscanner.alerts.pushbullet import PushBullet


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Main Window GUI
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # Additional GUI setup
        self.setWindowTitle(__appname__ + " " + __version__)
        self._set_resolution_limits()
        self.scene_init = QtGui.QGraphicsScene()
        self.scene_cycle = QtGui.QGraphicsScene()
        self.graphicsView_init.setScene(self.scene_init)
        self.graphicsView_cyclic.setScene(self.scene_cycle)

        # Status bar
        self.statusText = QtGui.QLabel("Ready")
        self.statusBar().addWidget(self.statusText, 1)

        # Restore GUI settings
        self.read_settings()

        # Thread initial config
        self.worker_thread = QtCore.QThread()
        self.image_processor = ImageProcessor()
        self.image_processor.moveToThread(self.worker_thread)
        self.image_processor.request_image.connect(self.image_request)
        self.image_processor.comparison_done.connect(self.comparison_done)
        self.image_processor.finished.connect(self.process_done)
        self.worker_thread.started.connect(self.image_processor.process)
        
        # Sound alarm system
        self.alarm_thread = QtCore.QThread()
        self.sound_alert = SoundAlert()
        self.sound_alert.moveToThread(self.alarm_thread)
        self.sound_alert.finished.connect(self.alarm_thread.quit)
        self.alarm_thread.started.connect(self.sound_alert.process)

        # Push notifications
        self.notif_thread = QtCore.QThread()
        self.push_bullet = PushBullet()
        self.push_bullet.moveToThread(self.notif_thread)
        self.push_bullet.finished.connect(self.notif_done)
        self.notif_thread.started.connect(self.push_bullet.process)

        # Signals
        self.pushButton_select.clicked.connect(self._btn_select_clicked)
        self.pushButton_start.clicked.connect(self._btn_start_clicked)
        self.pushButton_send_test_message.clicked.connect(self._btn_send_test_message)

    # -------------------------------------------------------------------------
    # Helper functions

    def _set_resolution_limits(self):
        screen_geom = ScanTools.get_full_screen_geometry()
        
        self.spinBox_x.setMinimum(screen_geom.x())
        self.spinBox_y.setMinimum(screen_geom.y())
        self.spinBox_x.setMaximum(screen_geom.x() + screen_geom.width())
        self.spinBox_y.setMaximum(screen_geom.y() + screen_geom.height())
        
        self.spinBox_width.setMaximum(screen_geom.width())
        self.spinBox_height.setMaximum(screen_geom.height())
    
    def _take_screenshot(self):
        return QtGui.QPixmap.grabWindow(
            QtGui.QApplication.desktop().winId(),
            self.screen_area.x(),
            self.screen_area.y(),
            self.screen_area.width(),
            self.screen_area.height()
            )
    
    def _draw_init_image(self, screenshot):
        pix_item = QtGui.QGraphicsPixmapItem(screenshot)
        self.scene_init.clear()
        self.scene_init.setSceneRect(screenshot.rect())
        self.scene_init.addItem(pix_item)
    
    def _draw_cycle_image(self, screenshot):
        pix_item = QtGui.QGraphicsPixmapItem(screenshot)
        self.scene_cycle.clear()
        self.scene_cycle.setSceneRect(screenshot.rect())
        self.scene_cycle.addItem(pix_item)

    # -------------------------------------------------------------------------
    # Alarm Handling

    def _send_notification(self):
        self.statusText.setStyleSheet("")  # reset stylesheet
        self.statusText.setText("Attempting to send notification...")

        api_key = self.lineEdit_pb_key.text()
        message_title = self.lineEdit_pb_title.text()
        message_body = self.textEdit_pb_message.toPlainText()

        self.push_bullet.set_message(
            api_key,
            message_title,
            message_body
        )

        self.notif_thread.start()

    def _handle_alarms(self):
        audio_enabled = self.checkBox_audio.isChecked()
        notification_enabled = self.checkBox_pushbullet.isChecked()

        # sound the alarm :)
        if audio_enabled:
            self.sound_alert.exiting = False
            self.alarm_thread.start()

        # send push notification
        if notification_enabled:
            self._send_notification()

        QtGui.QMessageBox.information(self, __appname__, "Threhsold exceeded.")

        if audio_enabled:
            self.sound_alert.exiting = True

    # -------------------------------------------------------------------------
    # Inter-thread communication

    @QtCore.Slot()
    def image_request(self):
        screenshot = self._take_screenshot()
        self._draw_cycle_image(screenshot)
        self.image_processor.set_cyclic_image(screenshot.toImage())
        
        self.image_processor.waitCondition.wakeOne()
    
    @QtCore.Slot(float)
    def comparison_done(self, result):
        self.lineEdit_result.setText("{0:.2f}".format(result))
    
    @QtCore.Slot(bool)
    def process_done(self, thr_exceeded):
        self.worker_thread.quit()
        
        while self.worker_thread.isRunning():
            time.sleep(0.01)
            self.image_processor.waitCondition.wakeOne()  # wake thread in case it's blocked at requesting an image
                
        self.pushButton_start.setText("Start")
        self.pushButton_start.setEnabled(True)

        if thr_exceeded:
            self._handle_alarms()

        self.statusText.setStyleSheet("")  # reset stylesheet
        self.statusText.setText("Ready")

    @QtCore.Slot(bool)
    def notif_done(self, response):
        self.notif_thread.quit()

        if response:
            self.statusText.setStyleSheet("QLabel {color: green;}")
            self.statusText.setText("Notification successfully sent")
        else:
            self.statusText.setStyleSheet("QLabel {color: red;}")
            self.statusText.setText("Failed to send notification")

        while self.notif_thread.isRunning():
            time.sleep(0.01)

        # re-enable the button - doesn't matter if the notification wasn't a test
        # synchronization problems between the test and the real alarm are minor
        self.pushButton_send_test_message.setEnabled(True)

    # -------------------------------------------------------------------------
    # Buttons

    @QtCore.Slot()
    def _btn_send_test_message(self):
        self.pushButton_send_test_message.setEnabled(False)
        self._send_notification()

    @QtCore.Slot()
    def _btn_select_clicked(self):
        trans_win = TransparentWindow()
        
        if trans_win.exec_():
            rubber_geom = trans_win.rubber_band.geometry()
            self.spinBox_x.setValue(rubber_geom.x())
            self.spinBox_y.setValue(rubber_geom.y())
            self.spinBox_width.setValue(rubber_geom.width())
            self.spinBox_height.setValue(rubber_geom.height())
    
    @QtCore.Slot()
    def _btn_start_clicked(self):
        if not self.worker_thread.isRunning():
            # Thread is not running and we wish to start it
            self.image_processor.exiting = False
            self.pushButton_start.setEnabled(False)

            self.statusText.setStyleSheet("")  # reset stylesheet
            self.statusText.setText("Running...")

            self.threshold = self.doubleSpinBox_thr.value()
            self.cycle_time = self.spinBox_cycle.value()
            self.screen_area = QtCore.QRect(
                self.spinBox_x.value(),
                self.spinBox_y.value(),
                self.spinBox_width.value(),
                self.spinBox_height.value())
            
            screenshot = self._take_screenshot()
            self._draw_init_image(screenshot)
            self.scene_cycle.clear()
            
            self.image_processor.config(self.threshold, self.cycle_time, screenshot.toImage())
            self.worker_thread.start()
            
            while not self.worker_thread.isRunning():
                time.sleep(0.01)
            
            self.pushButton_start.setText("Stop")
            self.pushButton_start.setEnabled(True)
        else:
            # Thread is running and we wish to stop it
            self.image_processor.exiting = True
            self.pushButton_start.setEnabled(False)

    # -------------------------------------------------------------------------
    # GUI Restoration

    def read_settings(self):
        self.settings = QtCore.QSettings(
            QtCore.QSettings.IniFormat,
            QtCore.QSettings.UserScope,
            __organization__,
            __appname__
        )

        self.settings.beginGroup("MainWindow")

        # Tab: Image Capture
        self.spinBox_x.setValue(
            int(self.settings.value("screen_x", 0))
        )
        self.spinBox_y.setValue(
            int(self.settings.value("screen_y", 0))
        )
        self.spinBox_width.setValue(
            int(self.settings.value("screen_width", 0))
        )
        self.spinBox_height.setValue(
            int(self.settings.value("screen_height", 0))
        )
        self.doubleSpinBox_thr.setValue(
            float(self.settings.value("threshold", 0))
        )
        self.spinBox_cycle.setValue(
            int(self.settings.value("cycle", 3))
        )

        # Tab: Options
        self.checkBox_audio.setChecked(
            True if self.settings.value("enable_audio", "true") == "true" else False
        )
        self.checkBox_pushbullet.setChecked(
            True if self.settings.value("enable_pushbullet", "false") == "true" else False
        )
        self.lineEdit_pb_key.setText(
            self.settings.value("pb_key", "YOUR-API-KEY-HERE")
        )
        self.lineEdit_pb_title.setText(
            self.settings.value("pb_title", "Alert")
        )
        self.textEdit_pb_message.setText(
            self.settings.value("pb_message", "Threshold exceeded.")
        )

        self.settings.endGroup()

    def write_settings(self):
        self.settings = QtCore.QSettings(
            QtCore.QSettings.IniFormat,
            QtCore.QSettings.UserScope,
            __organization__,
            __appname__
        )

        self.settings.beginGroup("MainWindow")

        # Tab: Image Capture
        self.settings.setValue(
            "screen_x",
            self.spinBox_x.value()
        )
        self.settings.setValue(
            "screen_y",
            self.spinBox_y.value()
        )
        self.settings.setValue(
            "screen_width",
            self.spinBox_width.value()
        )
        self.settings.setValue(
            "screen_height",
            self.spinBox_height.value()
        )
        self.settings.setValue(
            "threshold",
            self.doubleSpinBox_thr.value()
        )
        self.settings.setValue(
            "cycle",
            self.spinBox_cycle.value()
        )

        # Tab: Options
        self.settings.setValue(
            "enable_audio",
            self.checkBox_audio.isChecked()
        )
        self.settings.setValue(
            "enable_pushbullet",
            self.checkBox_pushbullet.isChecked()
        )
        self.settings.setValue(
            "pb_key",
            self.lineEdit_pb_key.text()
        )
        self.settings.setValue(
            "pb_title",
            self.lineEdit_pb_title.text()
        )
        self.settings.setValue(
            "pb_message",
            self.textEdit_pb_message.toPlainText()
        )

        self.settings.endGroup()

    # event: QCloseEvent
    def closeEvent(self, event):
        self.write_settings()
        event.accept()


def run():
    appl = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    appl.exec_()
