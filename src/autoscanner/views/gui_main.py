# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\gui_main.ui'
#
# Created: Sat Dec 12 18:33:37 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 510)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setAutoFillBackground(True)
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_3 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.graphicsView_init = QtGui.QGraphicsView(self.groupBox_3)
        self.graphicsView_init.setObjectName("graphicsView_init")
        self.verticalLayout.addWidget(self.graphicsView_init)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.graphicsView_cyclic = QtGui.QGraphicsView(self.groupBox_3)
        self.graphicsView_cyclic.setObjectName("graphicsView_cyclic")
        self.verticalLayout_2.addWidget(self.graphicsView_cyclic)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox_1 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_1.setObjectName("groupBox_1")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_1 = QtGui.QLabel(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_1.sizePolicy().hasHeightForWidth())
        self.label_1.setSizePolicy(sizePolicy)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout.addWidget(self.label_1)
        self.spinBox_x = QtGui.QSpinBox(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_x.sizePolicy().hasHeightForWidth())
        self.spinBox_x.setSizePolicy(sizePolicy)
        self.spinBox_x.setObjectName("spinBox_x")
        self.horizontalLayout.addWidget(self.spinBox_x)
        self.label_2 = QtGui.QLabel(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_y = QtGui.QSpinBox(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_y.sizePolicy().hasHeightForWidth())
        self.spinBox_y.setSizePolicy(sizePolicy)
        self.spinBox_y.setObjectName("spinBox_y")
        self.horizontalLayout.addWidget(self.spinBox_y)
        self.label_3 = QtGui.QLabel(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_width = QtGui.QSpinBox(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_width.sizePolicy().hasHeightForWidth())
        self.spinBox_width.setSizePolicy(sizePolicy)
        self.spinBox_width.setObjectName("spinBox_width")
        self.horizontalLayout.addWidget(self.spinBox_width)
        self.label_4 = QtGui.QLabel(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.spinBox_height = QtGui.QSpinBox(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_height.sizePolicy().hasHeightForWidth())
        self.spinBox_height.setSizePolicy(sizePolicy)
        self.spinBox_height.setObjectName("spinBox_height")
        self.horizontalLayout.addWidget(self.spinBox_height)
        self.pushButton_select = QtGui.QPushButton(self.groupBox_1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_select.sizePolicy().hasHeightForWidth())
        self.pushButton_select.setSizePolicy(sizePolicy)
        self.pushButton_select.setObjectName("pushButton_select")
        self.horizontalLayout.addWidget(self.pushButton_select)
        self.gridLayout_2.addWidget(self.groupBox_1, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_1)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.doubleSpinBox_thr = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_thr.setMaximum(100.0)
        self.doubleSpinBox_thr.setSingleStep(0.01)
        self.doubleSpinBox_thr.setObjectName("doubleSpinBox_thr")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox_thr)
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.spinBox_cycle = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_cycle.setToolTip("")
        self.spinBox_cycle.setStatusTip("")
        self.spinBox_cycle.setWhatsThis("")
        self.spinBox_cycle.setMinimum(1)
        self.spinBox_cycle.setMaximum(600)
        self.spinBox_cycle.setProperty("value", 3)
        self.spinBox_cycle.setObjectName("spinBox_cycle")
        self.horizontalLayout_2.addWidget(self.spinBox_cycle)
        self.label = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_result = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_result.sizePolicy().hasHeightForWidth())
        self.lineEdit_result.setSizePolicy(sizePolicy)
        self.lineEdit_result.setStyleSheet("background-color: rgb(242, 245, 255);")
        self.lineEdit_result.setMaxLength(16)
        self.lineEdit_result.setFrame(True)
        self.lineEdit_result.setReadOnly(True)
        self.lineEdit_result.setObjectName("lineEdit_result")
        self.horizontalLayout_2.addWidget(self.lineEdit_result)
        self.pushButton_start = QtGui.QPushButton(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_2.addWidget(self.pushButton_start)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setAutoFillBackground(True)
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_audio = QtGui.QCheckBox(self.groupBox)
        self.checkBox_audio.setChecked(True)
        self.checkBox_audio.setObjectName("checkBox_audio")
        self.verticalLayout_3.addWidget(self.checkBox_audio)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_pushbullet = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_pushbullet.setObjectName("checkBox_pushbullet")
        self.verticalLayout_5.addWidget(self.checkBox_pushbullet)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setWhatsThis("")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 3, 0, 1, 1)
        self.lineEdit_pb_key = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_pb_key.setObjectName("lineEdit_pb_key")
        self.gridLayout_4.addWidget(self.lineEdit_pb_key, 1, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 1, 0, 1, 1)
        self.lineEdit_pb_title = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_pb_title.setObjectName("lineEdit_pb_title")
        self.gridLayout_4.addWidget(self.lineEdit_pb_title, 2, 1, 1, 1)
        self.textEdit_pb_message = QtGui.QTextEdit(self.groupBox_4)
        self.textEdit_pb_message.setObjectName("textEdit_pb_message")
        self.gridLayout_4.addWidget(self.textEdit_pb_message, 3, 1, 1, 1)
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 2, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setOpenExternalLinks(True)
        self.label_12.setObjectName("label_12")
        self.gridLayout_4.addWidget(self.label_12, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.pushButton_send_test_message = QtGui.QPushButton(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_send_test_message.sizePolicy().hasHeightForWidth())
        self.pushButton_send_test_message.setSizePolicy(sizePolicy)
        self.pushButton_send_test_message.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pushButton_send_test_message.setObjectName("pushButton_send_test_message")
        self.verticalLayout_5.addWidget(self.pushButton_send_test_message)
        self.gridLayout_3.addWidget(self.groupBox_4, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Autoscanner", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Initial capture", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Cyclic capture", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_1.setTitle(QtGui.QApplication.translate("MainWindow", "Coordinates", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("MainWindow", "X:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Y:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Width:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Height:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_select.setText(QtGui.QApplication.translate("MainWindow", "Select Area", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "Control", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Threshold [%]:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Cycle time [s]:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Comparison result [%]:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QtGui.QApplication.translate("MainWindow", "Image Capture", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Sound", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_audio.setText(QtGui.QApplication.translate("MainWindow", "Enable audio warnings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Pushbullet", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_pushbullet.setText(QtGui.QApplication.translate("MainWindow", "Enable Pushbullet notifications", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Message:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Key:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Title:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><a href=\"https://www.pushbullet.com/\"><span style=\" text-decoration: underline; color:#0000ff;\">Don\'t have a key, yet?</span></a></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_send_test_message.setText(QtGui.QApplication.translate("MainWindow", "Send Test Message", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
