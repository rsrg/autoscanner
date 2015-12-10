"""
Created on 27 nov. 2015

@author: Valtyr Farshield
"""

import time

from PySide import QtCore
from autoscanner.tools.scantools import ScanTools


class ImageProcessor(QtCore.QObject):
    """
    Handles the comparison between images
    """
    waitCondition = QtCore.QWaitCondition()
    mutex = QtCore.QMutex()

    request_image = QtCore.Signal()
    comparison_done = QtCore.Signal(float)
    finished = QtCore.Signal(bool)

    def __init__(self, parent=None):
        super(ImageProcessor, self).__init__(parent)

        self.configured = False
        self.exiting = False
        self.threshold = None
        self.cycle_time = None
        self.img_init = None
        self.img_cyclic = None

    def config(self, threshold, cycle_time, img_init):
        self.threshold = threshold
        self.cycle_time = cycle_time
        self.img_init = img_init

        self.configured = True

    def set_cyclic_image(self, img_cyclic):
        self.img_cyclic = img_cyclic

    def process(self):
        thr_exceeded = False
        if self.configured:
            # convert initial image
            pil_img_init = ScanTools.convert_image(self.img_init)

            while not self.exiting:
                countdown = self.cycle_time

                while not self.exiting and countdown > 0:
                    time.sleep(1)
                    countdown -= 1

                if self.exiting:
                    break

                # request cyclic image
                self.request_image.emit()
                self.mutex.lock()
                self.waitCondition.wait(self.mutex, time=3600)
                self.mutex.unlock()

                if self.exiting:
                    break

                # convert cyclic image and compare images
                pil_img_cyclic = ScanTools.convert_image(self.img_cyclic)
                result = ScanTools.compare_images(pil_img_init, pil_img_cyclic)

                self.comparison_done.emit(result)

                if result > self.threshold:
                    thr_exceeded = True
                    break

        self.finished.emit(thr_exceeded)
