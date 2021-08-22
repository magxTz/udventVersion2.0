# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\settingMenu.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal as pys

class clickLabel(QtWidgets.QLabel):
    clicked=pys()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLabel.mousePressEvent(self,event)

class Ui_setting(object):
    def setupUi(self, setting):
        setting.setObjectName("setting")
        setting.resize(660, 550)
        setting.setStyleSheet("QWidget{\n"
"background:rgb(0,0,0);\n"
"\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #999999;\n"
"    height: 8px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #B1B1B1, stop:1 #c4c4c4);\n"
"    margin: 2px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);\n"
"    border: 1px solid #5c5c5c;\n"
"    width: 15px;\n"
"    margin: -2px 0; \n"
"    border-radius: 3px;\n"
"}\n"
"QCheckBox{\n"
"color:white;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(setting)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 70))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame.setStyleSheet("background-color: rgb(172, 47, 9);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 601, 62))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_17 = QtWidgets.QLabel(self.layoutWidget)
        self.label_17.setMinimumSize(QtCore.QSize(120, 24))
        self.label_17.setStyleSheet("color:beige;\n"
"background-color: transparent;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_17.setObjectName("label_17")
        self.verticalLayout_13.addWidget(self.label_17)
        self.trans_slider = QtWidgets.QSlider(self.layoutWidget)
        self.trans_slider.setMinimumSize(QtCore.QSize(160, 20))
        self.trans_slider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.trans_slider.setStyleSheet("border: 1px solid #222;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   \n"
"    margin: 2px 0;")
        self.trans_slider.setMinimum(0)
        self.trans_slider.setMaximum(100)
        self.trans_slider.setProperty("value", 70)
        self.trans_slider.setOrientation(QtCore.Qt.Horizontal)
        self.trans_slider.setObjectName("trans_slider")
        self.verticalLayout_13.addWidget(self.trans_slider)
        self.horizontalLayout_4.addLayout(self.verticalLayout_13)
        spacerItem = QtWidgets.QSpacerItem(100, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMaximumSize(QtCore.QSize(60, 60))
        self.label.setStyleSheet("background:transparent")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/resources/icons8_services_64px.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(254, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_11.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background:transparent")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:18px;\n"
"")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(428, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.eg = QtWidgets.QCheckBox(self.frame_2)
        self.eg.setChecked(True)
        self.eg.setObjectName("eg")
        self.verticalLayout_3.addWidget(self.eg)
        self.pg = QtWidgets.QCheckBox(self.frame_2)
        self.pg.setChecked(True)
        self.pg.setObjectName("pg")
        self.verticalLayout_3.addWidget(self.pg)
        self.frg = QtWidgets.QCheckBox(self.frame_2)
        self.frg.setChecked(True)
        self.frg.setObjectName("frg")
        self.verticalLayout_3.addWidget(self.frg)
        self.tvg = QtWidgets.QCheckBox(self.frame_2)
        self.tvg.setChecked(True)
        self.tvg.setObjectName("tvg")
        self.verticalLayout_3.addWidget(self.tvg)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.line_5 = QtWidgets.QFrame(self.frame_2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_5.addWidget(self.line_5)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, -1, 37, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.toggleSwitch_grid = QtWidgets.QFrame(self.frame_6)
        self.toggleSwitch_grid.setGeometry(QtCore.QRect(90, 10, 41, 21))
        self.toggleSwitch_grid.setMinimumSize(QtCore.QSize(41, 21))
        self.toggleSwitch_grid.setMaximumSize(QtCore.QSize(41, 21))
        self.toggleSwitch_grid.setStyleSheet("background:red;\n"
"border-radius:10px;")
        self.toggleSwitch_grid.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggleSwitch_grid.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggleSwitch_grid.setObjectName("toggleSwitch_grid")
        self.tg_g = QtWidgets.QPushButton(self.toggleSwitch_grid)
        self.tg_g.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.tg_g.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tg_g.setFont(font)
        self.tg_g.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"border-radius:10px;\n"
"color:red;")
        self.tg_g.setFlat(True)
        self.tg_g.setObjectName("tg_g")
        self.label_16 = QtWidgets.QLabel(self.frame_6)
        self.label_16.setGeometry(QtCore.QRect(20, 0, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color:white")
        self.label_16.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_12.addWidget(self.frame_6)
        self.embbed = QtWidgets.QRadioButton(self.frame_2)
        self.embbed.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"font: bold;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.embbed.setObjectName("embbed")
        self.verticalLayout_12.addWidget(self.embbed)
        self.separate = QtWidgets.QRadioButton(self.frame_2)
        self.separate.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"font: bold;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.separate.setObjectName("separate")
        self.verticalLayout_12.addWidget(self.separate)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fwSlider = QtWidgets.QSlider(self.frame_2)
        self.fwSlider.setCursor(QtGui.QCursor(QtCore.Qt.SizeHorCursor))
        self.fwSlider.setStyleSheet("border: 1px solid #222;\n"
"    height: 8px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */\n"
"   \n"
"    margin: 2px 0;")
        self.fwSlider.setMinimum(10)
        self.fwSlider.setMaximum(255)
        self.fwSlider.setOrientation(QtCore.Qt.Horizontal)
        self.fwSlider.setObjectName("fwSlider")
        self.horizontalLayout_3.addWidget(self.fwSlider)
        self.fweight = QtWidgets.QLabel(self.frame_2)
        self.fweight.setMinimumSize(QtCore.QSize(45, 0))
        self.fweight.setMaximumSize(QtCore.QSize(40, 16777215))
        self.fweight.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.fweight.setObjectName("fweight")
        self.horizontalLayout_3.addWidget(self.fweight)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setObjectName("gridLayout")
        self.toggleSwitch = QtWidgets.QFrame(self.frame_4)
        self.toggleSwitch.setMinimumSize(QtCore.QSize(41, 21))
        self.toggleSwitch.setMaximumSize(QtCore.QSize(60, 21))
        self.toggleSwitch.setStyleSheet("background:red;\n"
"border-radius:10px;")
        self.toggleSwitch.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.toggleSwitch.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toggleSwitch.setObjectName("toggleSwitch")
        self.tg = QtWidgets.QPushButton(self.toggleSwitch)
        self.tg.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.tg.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tg.setFont(font)
        self.tg.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"border-radius:10px;\n"
"color:red;")
        self.tg.setFlat(True)
        self.tg.setObjectName("tg")
        self.gridLayout.addWidget(self.toggleSwitch, 0, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.frame_4)
        self.label_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_4)
        self.label_15.setMinimumSize(QtCore.QSize(30, 0))
        self.label_15.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_15.setStyleSheet("color:white")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 1, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_6.addWidget(self.line_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.debug_tg = QtWidgets.QFrame(self.frame_5)
        self.debug_tg.setGeometry(QtCore.QRect(10, 0, 60, 21))
        self.debug_tg.setMinimumSize(QtCore.QSize(60, 21))
        self.debug_tg.setMaximumSize(QtCore.QSize(41, 21))
        self.debug_tg.setStyleSheet("background:red;\n"
"border-radius:10px;")
        self.debug_tg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.debug_tg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.debug_tg.setObjectName("debug_tg")
        self.tg_btn = QtWidgets.QPushButton(self.debug_tg)
        self.tg_btn.setGeometry(QtCore.QRect(0, 0, 20, 20))
        self.tg_btn.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tg_btn.setFont(font)
        self.tg_btn.setStyleSheet("background-color: rgb(248, 248, 248);\n"
"border-radius:10px;\n"
"color:red;")
        self.tg_btn.setFlat(True)
        self.tg_btn.setObjectName("tg_btn")
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_11.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setStyleSheet("background:transparent;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:16px;\n"
"")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_8.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(388, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"\n"
"")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_12.addWidget(self.label_8)
        spacerItem7 = QtWidgets.QSpacerItem(188, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem7)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pdial = QtWidgets.QDial(self.frame_3)
        self.pdial.setMaximum(100)
        self.pdial.setWrapping(False)
        self.pdial.setNotchTarget(0.7)
        self.pdial.setNotchesVisible(True)
        self.pdial.setObjectName("pdial")
        self.horizontalLayout_11.addWidget(self.pdial)
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_11.addWidget(self.line_3)
        self.peepdial = QtWidgets.QDial(self.frame_3)
        self.peepdial.setMinimum(5)
        self.peepdial.setMaximum(20)
        self.peepdial.setNotchTarget(19.7)
        self.peepdial.setNotchesVisible(True)
        self.peepdial.setObjectName("peepdial")
        self.horizontalLayout_11.addWidget(self.peepdial)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        self.pdValue = clickLabel(self.frame_3)
        self.pdValue.setMinimumSize(QtCore.QSize(40, 20))
        self.pdValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.pdValue.setAlignment(QtCore.Qt.AlignCenter)
        self.pdValue.setObjectName("pdValue")
        self.horizontalLayout_9.addWidget(self.pdValue)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_9)
        spacerItem8 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.peepValue = clickLabel(self.frame_3)
        self.peepValue.setMinimumSize(QtCore.QSize(40, 20))
        self.peepValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.peepValue.setAlignment(QtCore.Qt.AlignCenter)
        self.peepValue.setObjectName("peepValue")
        self.horizontalLayout_10.addWidget(self.peepValue)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_7.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        self.brSlider = QtWidgets.QSlider(self.frame_3)
        self.brSlider.setMinimum(10)
        self.brSlider.setMaximum(30)
        self.brSlider.setProperty("value", 12)
        self.brSlider.setOrientation(QtCore.Qt.Horizontal)
        self.brSlider.setObjectName("brSlider")
        self.horizontalLayout_18.addWidget(self.brSlider)
        self.brValue = clickLabel(self.frame_3)
        self.brValue.setMinimumSize(QtCore.QSize(40, 20))
        self.brValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.brValue.setAlignment(QtCore.Qt.AlignCenter)
        self.brValue.setObjectName("brValue")
        self.horizontalLayout_18.addWidget(self.brValue)
        self.verticalLayout_7.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_17.addLayout(self.verticalLayout_7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem10 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem10)
        self.line_4 = QtWidgets.QFrame(self.frame_3)
        self.line_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_16.addWidget(self.line_4)
        spacerItem11 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.horizontalLayout_17.addLayout(self.horizontalLayout_16)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"\n"
"")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_14.addWidget(self.label_11)
        spacerItem13 = QtWidgets.QSpacerItem(148, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tvdial = QtWidgets.QDial(self.frame_3)
        self.tvdial.setMaximum(1000)
        self.tvdial.setWrapping(False)
        self.tvdial.setNotchTarget(10.7)
        self.tvdial.setNotchesVisible(True)
        self.tvdial.setObjectName("tvdial")
        self.verticalLayout_8.addWidget(self.tvdial)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem14)
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_15.addWidget(self.label_12)
        self.tvValue = clickLabel(self.frame_3)
        self.tvValue.setMinimumSize(QtCore.QSize(40, 20))
        self.tvValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.tvValue.setAlignment(QtCore.Qt.AlignCenter)
        self.tvValue.setObjectName("tvValue")
        self.horizontalLayout_15.addWidget(self.tvValue)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem15)
        self.verticalLayout_8.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-family:verdana;\n"
"font-size:12px;\n"
"")
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_21.addWidget(self.label_14)
        self.frSlider = QtWidgets.QSlider(self.frame_3)
        self.frSlider.setOrientation(QtCore.Qt.Horizontal)
        self.frSlider.setObjectName("frSlider")
        self.horizontalLayout_21.addWidget(self.frSlider)
        self.frValue = clickLabel(self.frame_3)
        self.frValue.setMinimumSize(QtCore.QSize(40, 20))
        self.frValue.setStyleSheet("color:beige;\n"
"font-size:15px;\n"
"border:1px solid beige;\n"
"border-radius:5px;\n"
"")
        self.frValue.setAlignment(QtCore.Qt.AlignCenter)
        self.frValue.setObjectName("frValue")
        self.horizontalLayout_21.addWidget(self.frValue)
        self.verticalLayout_8.addLayout(self.horizontalLayout_21)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.horizontalLayout_17.addLayout(self.verticalLayout_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setContentsMargins(-1, 9, -1, -1)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem16)
        self.confirmChanges = QtWidgets.QPushButton(self.frame_3)
        self.confirmChanges.setMinimumSize(QtCore.QSize(150, 20))
        self.confirmChanges.setMaximumSize(QtCore.QSize(150, 16777215))
        self.confirmChanges.setStyleSheet("color:beige;\n"
"font:bold;\n"
"font-size:15px;\n"
"border-radius:10px;\n"
"background:rgb(188, 82, 51);")
        self.confirmChanges.setAutoDefault(False)
        self.confirmChanges.setDefault(False)
        self.confirmChanges.setFlat(False)
        self.confirmChanges.setObjectName("confirmChanges")
        self.horizontalLayout_20.addWidget(self.confirmChanges)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem17)
        self.verticalLayout_10.addLayout(self.horizontalLayout_20)
        self.verticalLayout_11.addWidget(self.frame_3)
        setting.setCentralWidget(self.centralwidget)

        self.retranslateUi(setting)
        self.pdial.valueChanged['int'].connect(self.pdValue.setNum)
        self.peepdial.valueChanged['int'].connect(self.peepValue.setNum)
        self.tvdial.valueChanged['int'].connect(self.tvValue.setNum)
        self.brSlider.valueChanged['int'].connect(self.brValue.setNum)
        self.frSlider.valueChanged['int'].connect(self.frValue.setNum)
        self.fwSlider.valueChanged['int'].connect(self.fweight.setNum)
        QtCore.QMetaObject.connectSlotsByName(setting)

    def retranslateUi(self, setting):
        _translate = QtCore.QCoreApplication.translate
        setting.setWindowTitle(_translate("setting", "setting"))
        self.label_17.setText(_translate("setting", "Form Transparency"))
        self.label_2.setText(_translate("setting", "Appearance"))
        self.label_3.setText(_translate("setting", "Hide/Show"))
        self.eg.setText(_translate("setting", "ECG Graph"))
        self.pg.setText(_translate("setting", "pressure Graph"))
        self.frg.setText(_translate("setting", "frow rate Graph"))
        self.tvg.setText(_translate("setting", "tidal volume Graph"))
        self.tg_g.setText(_translate("setting", "0"))
        self.label_16.setText(_translate("setting", "Gridlines"))
        self.embbed.setText(_translate("setting", "embbed in1 plot"))
        self.separate.setText(_translate("setting", "Separate"))
        self.label_4.setText(_translate("setting", "fill weight"))
        self.fweight.setText(_translate("setting", "10"))
        self.tg.setText(_translate("setting", "0"))
        self.label_5.setText(_translate("setting", "unfill"))
        self.label_15.setText(_translate("setting", "fill"))
        self.label_6.setText(_translate("setting", "Debug Mode"))
        self.tg_btn.setText(_translate("setting", "0"))
        self.label_7.setText(_translate("setting", "Control Variables"))
        self.label_8.setText(_translate("setting", "Pressure"))
        self.label_9.setText(_translate("setting", "Pdelta"))
        self.pdValue.setText(_translate("setting", "1"))
        self.label_10.setText(_translate("setting", "Peep"))
        self.peepValue.setText(_translate("setting", "1"))
        self.label_13.setText(_translate("setting", "Breath rate"))
        self.brValue.setText(_translate("setting", "1"))
        self.label_11.setText(_translate("setting", "Tidal Volume"))
        self.label_12.setText(_translate("setting", "Volume"))
        self.tvValue.setText(_translate("setting", "1"))
        self.label_14.setText(_translate("setting", "flow Rate"))
        self.frValue.setText(_translate("setting", "1"))
        self.confirmChanges.setText(_translate("setting", "Confirm Changes"))

import udvent_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setting = QtWidgets.QMainWindow()
    ui = Ui_setting()
    ui.setupUi(setting)
    setting.show()
    sys.exit(app.exec_())

