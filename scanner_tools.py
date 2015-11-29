'''
Created on 22 nov. 2015

@author: Valtyr Farshield
'''
import sys
import cStringIO
import Image

from itertools import izip
from PySide import QtGui, QtCore

class ScannerTools():
    
    @staticmethod
    def getFullScreenGeometry():
        full_screen_geometry = QtCore.QRect()
        for screen_id in range(QtGui.QDesktopWidget().screenCount()):
            full_screen_geometry = full_screen_geometry.united(
                QtGui.QDesktopWidget().screenGeometry(screen=screen_id))
        return full_screen_geometry
    
    @staticmethod
    def convertImage(img):
        buffer1 = QtCore.QBuffer()
        buffer1.open(QtCore.QIODevice.ReadWrite)
        img.save(buffer1, "PNG")
        
        strio = cStringIO.StringIO()
        strio.write(buffer1.data())
        buffer1.close()
        strio.seek(0)
        
        return Image.open(strio)
    
    @staticmethod
    def compareImages(pil_img1, pil_img2):
        pairs = izip(pil_img1.getdata(), pil_img2.getdata())
        if len(pil_img1.getbands()) == 1:
            # for gray-scale jpegs
            dif = sum(abs(p1-p2) for p1,p2 in pairs)
        else:
            dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))
         
        ncomponents = pil_img1.size[0] * pil_img1.size[1] * 3
        
        return (dif / 255.0 * 100) / ncomponents

def main():
    QtGui.QApplication(sys.argv)
    print ScannerTools.getFullScreenGeometry()

if __name__ == '__main__':
    main()
