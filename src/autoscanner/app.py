"""
Created on 22 nov. 2015

@author: Valtyr Farshield
"""

import sys
import time
from PySide import QtGui, QtCore

from autoscanner import __appname__
from autoscanner.views.gui_main import Ui_MainWindow
from autoscanner.views.gui_transparent import TransparentWindow
from autoscanner.tools.scantools import ScanTools
from autoscanner.tools.imageprocessor import ImageProcessor
from autoscanner.alerts.soundalert import SoundAlert


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Main Window GUI
    """
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # Additional GUI setup
        self.setWindowTitle(__appname__)
        self._set_resolution_limits()
        self.scene_init = QtGui.QGraphicsScene()
        self.scene_cycle = QtGui.QGraphicsScene()
        self.graphicsView_init.setScene(self.scene_init)
        self.graphicsView_cyclic.setScene(self.scene_cycle)
        
        # Thread initial config
        self.worker_thread = QtCore.QThread()
        self.image_processor = ImageProcessor()
        self.image_processor.moveToThread(self.worker_thread)
        self.image_processor.request_image.connect(self.image_request)
        self.image_processor.comparison_done.connect(self.comparison_done)
        self.image_processor.finished.connect(self.process_done)
        self.worker_thread.started.connect(self.image_processor.process)
        
        # Alarm system
        self.alarm_thread = QtCore.QThread()
        self.red_alert = SoundAlert()
        self.red_alert.moveToThread(self.alarm_thread)
        self.red_alert.finished.connect(self.alarm_thread.quit)
        self.alarm_thread.started.connect(self.red_alert.process)
        
        # Signals
        self.pushButton_select.clicked.connect(self._btn_select_clicked)
        self.pushButton_start.clicked.connect(self._btn_start_clicked)
    
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
            self.red_alert.exiting = False
            self.alarm_thread.start()
            QtGui.QMessageBox.information(self, __appname__, "Threhsold exceeded")
            self.red_alert.exiting = True
    
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


def run():
    appl = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    appl.exec_()
