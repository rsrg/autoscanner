'''
Created on 22 nov. 2015

@author: Valtyr Farshield
'''

import sys
import time
from PySide import QtGui, QtCore

from autoscanner.view.gui_main import Ui_MainWindow
from autoscanner.view.gui_transparent import TransparentWindow
from autoscanner.controller.scantools import ScanTools
from autoscanner.controller.redalert import RedAlert

__appname__ = "Autoscanner 0.1"

waitCondition = QtCore.QWaitCondition()
mutex = QtCore.QMutex()

class ImageProcessor(QtCore.QObject):
    ''' Image Processor '''
    
    request_image = QtCore.Signal()
    comparison_done = QtCore.Signal(float)
    finished = QtCore.Signal(bool)
    
    def __init__(self, parent=None):
        super(ImageProcessor, self).__init__(parent)
        
        self.configured = False
        self.exiting = False
    
    def config(self, threshold, cycle_time, img_init):
        self.threshold = threshold
        self.cycle_time = cycle_time
        self.img_init = img_init
        
        self.configured = True
    
    def setCyclicImage(self, img_cyclic):
        self.img_cyclic = img_cyclic

    def process(self):
        thr_exceeded = False
        if self.configured:
            # convert initial image
            pil_img_init = ScanTools.convertImage(self.img_init)
            
            while not self.exiting:
                countdown = self.cycle_time
                
                while not self.exiting and countdown > 0:
                    time.sleep(1)
                    countdown -= 1

                if self.exiting: break

                # request cyclic image
                self.request_image.emit()
                mutex.lock()
                waitCondition.wait(mutex, time=3600)
                mutex.unlock()

                if self.exiting: break

                # convert cyclic image and compare images
                pil_img_cyclic = ScanTools.convertImage(self.img_cyclic)
                result = ScanTools.compareImages(pil_img_init, pil_img_cyclic)

                self.comparison_done.emit(result)

                if result > self.threshold:
                    thr_exceeded = True
                    break
        
        self.finished.emit(thr_exceeded)
        
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        # Additional GUI setup
        self.setWindowTitle(__appname__)
        self._setResolutionLimits()
        self.scene_init = QtGui.QGraphicsScene()
        self.scene_cycle = QtGui.QGraphicsScene()
        self.graphicsView_init.setScene(self.scene_init)
        self.graphicsView_cyclic.setScene(self.scene_cycle)
        
        # Thread initial config
        self.worker_thread = QtCore.QThread()
        self.image_processor = ImageProcessor()
        self.image_processor.moveToThread(self.worker_thread)
        self.image_processor.request_image.connect(self.imageRequest)
        self.image_processor.comparison_done.connect(self.comparisonDone)
        self.image_processor.finished.connect(self.processDone)
        self.worker_thread.started.connect(self.image_processor.process)
        
        # Alarm system
        self.alarm_thread = QtCore.QThread()
        self.red_alert = RedAlert()
        self.red_alert.moveToThread(self.alarm_thread)
        self.red_alert.finished.connect(self.alarm_thread.quit)
        self.alarm_thread.started.connect(self.red_alert.process)
        
        # Signals
        self.pushButton_select.clicked.connect(self._btnSelectClicked)
        self.pushButton_start.clicked.connect(self._btnStartClicked)
    
    def _setResolutionLimits(self):
        screen_geom = ScanTools.getFullScreenGeometry()
        
        self.spinBox_x.setMinimum(screen_geom.x())
        self.spinBox_y.setMinimum(screen_geom.y())
        self.spinBox_x.setMaximum(screen_geom.x() + screen_geom.width())
        self.spinBox_y.setMaximum(screen_geom.y() + screen_geom.height())
        
        self.spinBox_width.setMaximum(screen_geom.width())
        self.spinBox_height.setMaximum(screen_geom.height())
    
    def _takeScreenshot(self):
        return QtGui.QPixmap.grabWindow(
            QtGui.QApplication.desktop().winId(),
            self.screen_area.x(),
            self.screen_area.y(),
            self.screen_area.width(),
            self.screen_area.height()
            )
    
    def _drawInitImage(self, screenshot):
        pix_item = QtGui.QGraphicsPixmapItem(screenshot)
        self.scene_init.clear()
        self.scene_init.setSceneRect(screenshot.rect())
        self.scene_init.addItem(pix_item)
    
    def _drawCycleImage(self, screenshot):
        pix_item = QtGui.QGraphicsPixmapItem(screenshot)
        self.scene_cycle.clear()
        self.scene_cycle.setSceneRect(screenshot.rect())
        self.scene_cycle.addItem(pix_item)
        
    @QtCore.Slot()
    def imageRequest(self):
        screenshot = self._takeScreenshot()
        self._drawCycleImage(screenshot)
        self.image_processor.setCyclicImage(screenshot.toImage())
        
        waitCondition.wakeOne()
    
    @QtCore.Slot(float)
    def comparisonDone(self, result):
        self.lineEdit_result.setText("{0:.2f}".format(result))
    
    @QtCore.Slot(bool)
    def processDone(self, thr_exceeded):
        self.worker_thread.quit()
        
        while self.worker_thread.isRunning():
            time.sleep(0.01)
            waitCondition.wakeOne()  # wake thread in case it's blocked at requesting an image
                
        self.pushButton_start.setText("Start")
        self.pushButton_start.setEnabled(True)
        
        if thr_exceeded:
            self.red_alert.exiting = False
            self.alarm_thread.start()
            QtGui.QMessageBox.information(self, __appname__, "Threhsold exceeded")
            self.red_alert.exiting = True
    
    @QtCore.Slot()
    def _btnSelectClicked(self):
        trans_win = TransparentWindow()
        
        if trans_win.exec_():
            rubber_geom = trans_win.rubber_band.geometry()
            self.spinBox_x.setValue(rubber_geom.x())
            self.spinBox_y.setValue(rubber_geom.y())
            self.spinBox_width.setValue(rubber_geom.width())
            self.spinBox_height.setValue(rubber_geom.height())
    
    @QtCore.Slot()
    def _btnStartClicked(self):
        if self.worker_thread.isRunning() == False:
            ''' Thread is not running and we wish to start it '''
            self.image_processor.exiting = False
            self.pushButton_start.setEnabled(False)
            
            self.threshold = self.doubleSpinBox_thr.value()
            self.cycle_time = self.spinBox_cycle.value()
            self.screen_area = QtCore.QRect(
                self.spinBox_x.value(),
                self.spinBox_y.value(),
                self.spinBox_width.value(),
                self.spinBox_height.value())
            
            screenshot = self._takeScreenshot()
            self._drawInitImage(screenshot)
            self.scene_cycle.clear()
            
            self.image_processor.config(self.threshold, self.cycle_time, screenshot.toImage())
            self.worker_thread.start()
            
            while not self.worker_thread.isRunning():
                time.sleep(0.01)
            
            self.pushButton_start.setText("Stop")
            self.pushButton_start.setEnabled(True)
        else:
            ''' Thread is running and we wish to stop it '''
            self.image_processor.exiting = True
            self.pushButton_start.setEnabled(False)

def run():
    appl = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    appl.exec_()
