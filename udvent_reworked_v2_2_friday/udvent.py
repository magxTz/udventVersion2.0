# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\udVent_version3_improved_2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ventilator(object):
    def setupUi(self, Ventilator):
        Ventilator.setObjectName("Ventilator")
        Ventilator.resize(700, 522)
        Ventilator.setWindowOpacity(1.0)
        Ventilator.setStyleSheet("QWidget{\n"
"background:rgb(42, 42, 42);\n"
"}\n"
"QFrame#notification{\n"
"  border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(61, 203, 244);\n"
"border-radius:5px;\n"
"}\n"
"QFrame#notification:hover{\n"
"  background-color: rgb(61, 203, 244);\n"
"}\n"
"QFrame#notification:pressed{\n"
"background-color: rgb(172, 172, 172);}\n"
"\n"
"QFrame#infoFrame{\n"
"  border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgb(61, 203, 244);\n"
"}\n"
"QPushButton#setting,#notifications,#filter,#emegency{ \n"
"  border-width: 1px;\n"
"    border-style: solid;\n"
"    border-color: rgb(61, 203, 244);\n"
"border-radius:5px;\n"
"\n"
"}\n"
"QPushButton#setting:hover,#filter:hover,#notifications:hover,#startVent:hover,#emegency:hover{ \n"
"\n"
"    background-color: rgb(61, 203, 244);\n"
"}\n"
"QPushButton#setting:pressed,#filter:pressed,#notifications:pressed,#startVent:pressed,#emegency:pressed{ \n"
"\n"
"    background-color: rgb(172, 172, 172);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #05B8CC;\n"
"    width: 20px;\n"
"margin:0.5px\n"
"}\n"
"QGraphicsView{\n"
"border:none;\n"
"background:rgb(42, 42, 42);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(Ventilator)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.infoFrame = QtWidgets.QFrame(self.centralwidget)
        self.infoFrame.setMaximumSize(QtCore.QSize(110, 640))
        self.infoFrame.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"border-radius:10px;")
        self.infoFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.infoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoFrame.setLineWidth(4)
        self.infoFrame.setMidLineWidth(2)
        self.infoFrame.setObjectName("infoFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.infoFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_14 = QtWidgets.QLabel(self.infoFrame)
        self.label_14.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_6.addWidget(self.label_14)
        self.peep_label = QtWidgets.QLabel(self.infoFrame)
        self.peep_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(194, 52, 11);\n"
"font-size:14px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.peep_label.setAlignment(QtCore.Qt.AlignCenter)
        self.peep_label.setObjectName("peep_label")
        self.horizontalLayout_6.addWidget(self.peep_label)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_15 = QtWidgets.QLabel(self.infoFrame)
        self.label_15.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(61, 203, 244);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_7.addWidget(self.label_15)
        self.pressure_label = QtWidgets.QLabel(self.infoFrame)
        self.pressure_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(61, 203, 244);\n"
"font-size:18px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.pressure_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_label.setObjectName("pressure_label")
        self.horizontalLayout_7.addWidget(self.pressure_label)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_10 = QtWidgets.QLabel(self.infoFrame)
        self.label_10.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_4.addWidget(self.label_10)
        self.br_label = QtWidgets.QLabel(self.infoFrame)
        self.br_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(194, 52, 11);\n"
"font-size:18px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.br_label.setAlignment(QtCore.Qt.AlignCenter)
        self.br_label.setObjectName("br_label")
        self.horizontalLayout_4.addWidget(self.br_label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.infoFrame)
        self.label_11.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(61, 203, 244);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.frMax_label = QtWidgets.QLabel(self.infoFrame)
        self.frMax_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(61, 203, 244);\n"
"font-size:18px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.frMax_label.setAlignment(QtCore.Qt.AlignCenter)
        self.frMax_label.setObjectName("frMax_label")
        self.horizontalLayout_5.addWidget(self.frMax_label)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.infoFrame)
        self.label_5.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.tidalVolume_label = QtWidgets.QLabel(self.infoFrame)
        self.tidalVolume_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(194, 52, 11);\n"
"font-size:20px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.tidalVolume_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tidalVolume_label.setObjectName("tidalVolume_label")
        self.horizontalLayout_2.addWidget(self.tidalVolume_label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.infoFrame)
        self.label_7.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(61, 203, 244);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.tidalVolumeMin_label = QtWidgets.QLabel(self.infoFrame)
        self.tidalVolumeMin_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(61, 203, 244);\n"
"font-size:20px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.tidalVolumeMin_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tidalVolumeMin_label.setObjectName("tidalVolumeMin_label")
        self.horizontalLayout_3.addWidget(self.tidalVolumeMin_label)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.infoFrame)
        self.label_2.setMinimumSize(QtCore.QSize(90, 90))
        self.label_2.setMaximumSize(QtCore.QSize(90, 90))
        self.label_2.setStyleSheet("border:none;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/resources/icons8_lungs_96px_1.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.infoFrame)
        self.line.setStyleSheet("background:rgba(61, 203, 244,100);\n"
"")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.infoFrame)
        self.label_3.setMaximumSize(QtCore.QSize(35, 35))
        self.label_3.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(61, 203, 244);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.hbr_label = QtWidgets.QLabel(self.infoFrame)
        self.hbr_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:white;\n"
"font-size:24px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.hbr_label.setAlignment(QtCore.Qt.AlignCenter)
        self.hbr_label.setObjectName("hbr_label")
        self.horizontalLayout.addWidget(self.hbr_label)
        self.label_9 = QtWidgets.QLabel(self.infoFrame)
        self.label_9.setMinimumSize(QtCore.QSize(30, 20))
        self.label_9.setMaximumSize(QtCore.QSize(30, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:white;")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_20 = QtWidgets.QLabel(self.infoFrame)
        self.label_20.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_9.addWidget(self.label_20)
        self.feo2_label = QtWidgets.QLabel(self.infoFrame)
        self.feo2_label.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(194, 52, 11);\n"
"font-size:18px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39)\n"
"")
        self.feo2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.feo2_label.setObjectName("feo2_label")
        self.horizontalLayout_9.addWidget(self.feo2_label)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.label = QtWidgets.QLabel(self.infoFrame)
        self.label.setMinimumSize(QtCore.QSize(90, 90))
        self.label.setMaximumSize(QtCore.QSize(90, 90))
        self.label.setStyleSheet("border:none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/resources/icons8_anatomical_heart_96px.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_2.addWidget(self.infoFrame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(110, 300))
        self.frame_2.setMaximumSize(QtCore.QSize(110, 16777215))
        font = QtGui.QFont()
        font.setKerning(True)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_29 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_10.addWidget(self.label_29)
        self.status = QtWidgets.QLabel(self.frame_2)
        self.status.setMinimumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.status.setFont(font)
        self.status.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.horizontalLayout_10.addWidget(self.status)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_18 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:24px;\n"
"background:rgb(39, 39, 39)")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_11.addWidget(self.label_18)
        self.pr = QtWidgets.QLabel(self.frame_2)
        self.pr.setMinimumSize(QtCore.QSize(50, 50))
        self.pr.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(61, 203, 244);\n"
"font-size:20px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39);\n"
"border-radius:5px;\n"
"")
        self.pr.setAlignment(QtCore.Qt.AlignCenter)
        self.pr.setObjectName("pr")
        self.horizontalLayout_11.addWidget(self.pr)
        self.verticalLayout_7.addLayout(self.horizontalLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_22 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:18px;\n"
"background:rgb(39, 39, 39)")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_12.addWidget(self.label_22)
        self.frr = QtWidgets.QLabel(self.frame_2)
        self.frr.setMinimumSize(QtCore.QSize(50, 50))
        self.frr.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(61, 203, 244);\n"
"font-size:18px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39);\n"
"border-radius:5px;\n"
"")
        self.frr.setAlignment(QtCore.Qt.AlignCenter)
        self.frr.setObjectName("frr")
        self.horizontalLayout_12.addWidget(self.frr)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem2)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_27 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:18px;\n"
"background:rgb(39, 39, 39)")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_14.addWidget(self.label_27)
        self.tvr = QtWidgets.QLabel(self.frame_2)
        self.tvr.setMinimumSize(QtCore.QSize(50, 50))
        self.tvr.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgb(61, 203, 244);\n"
"font-size:18px;\n"
"font:bold;\n"
"background:rgb(39, 39, 39);\n"
"border-radius:5px;\n"
"")
        self.tvr.setAlignment(QtCore.Qt.AlignCenter)
        self.tvr.setObjectName("tvr")
        self.horizontalLayout_14.addWidget(self.tvr)
        self.verticalLayout_7.addLayout(self.horizontalLayout_14)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_28 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:18px;\n"
"background:rgb(39, 39, 39)")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_5.addWidget(self.label_28)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_30 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_15.addWidget(self.label_30)
        self.status_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.status_2.setFont(font)
        self.status_2.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(255,255,255);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.status_2.setAlignment(QtCore.Qt.AlignCenter)
        self.status_2.setObjectName("status_2")
        self.horizontalLayout_15.addWidget(self.status_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_31 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_16.addWidget(self.label_31)
        self.status_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.status_3.setFont(font)
        self.status_3.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(255,255,255);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.status_3.setAlignment(QtCore.Qt.AlignCenter)
        self.status_3.setObjectName("status_3")
        self.horizontalLayout_16.addWidget(self.status_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_32 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.horizontalLayout_17.addWidget(self.label_32)
        self.status_4 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.status_4.setFont(font)
        self.status_4.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(255,255,255);\n"
"font-size:10px;\n"
"background:rgb(39, 39, 39)")
        self.status_4.setAlignment(QtCore.Qt.AlignCenter)
        self.status_4.setObjectName("status_4")
        self.horizontalLayout_17.addWidget(self.status_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_17)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.label_34 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:18px;\n"
"background:rgb(39, 39, 39)")
        self.label_34.setText("")
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_7.addWidget(self.label_34)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
        self.label_33 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("cursive")
        font.setPointSize(-1)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet("border:none;\n"
"font-family:cursive;\n"
"color:rgba(194, 52, 11);\n"
"font-size:12px;\n"
"background:rgb(39, 39, 39)")
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_7.addWidget(self.label_33)
        self.thermometer = QtWidgets.QFrame(self.frame_2)
        self.thermometer.setMinimumSize(QtCore.QSize(90, 100))
        self.thermometer.setMaximumSize(QtCore.QSize(16777215, 100))
        self.thermometer.setStyleSheet("")
        self.thermometer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.thermometer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.thermometer.setObjectName("thermometer")
        self.layoutWidget = QtWidgets.QWidget(self.thermometer)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 0, 22, 91))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.fmax = QtWidgets.QLabel(self.layoutWidget)
        self.fmax.setMinimumSize(QtCore.QSize(0, 16))
        self.fmax.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.fmax.setFont(font)
        self.fmax.setStyleSheet("background:green;\n"
" color:white;\n"
"")
        self.fmax.setAlignment(QtCore.Qt.AlignCenter)
        self.fmax.setObjectName("fmax")
        self.verticalLayout_4.addWidget(self.fmax)
        self.fr_prog = QtWidgets.QFrame(self.layoutWidget)
        self.fr_prog.setMinimumSize(QtCore.QSize(20, 70))
        self.fr_prog.setMaximumSize(QtCore.QSize(20, 70))
        self.fr_prog.setStyleSheet("background-color: beige;\n"
"border-radius:5px;")
        self.fr_prog.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_prog.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_prog.setObjectName("fr_prog")
        self.fr_progl = QtWidgets.QLabel(self.fr_prog)
        self.fr_progl.setGeometry(QtCore.QRect(0, 50, 20, 5))
        self.fr_progl.setStyleSheet("background-color:rgb(255, 69, 32);\n"
"color:white;\n"
"font-size:11px;\n"
"")
        self.fr_progl.setText("")
        self.fr_progl.setAlignment(QtCore.Qt.AlignCenter)
        self.fr_progl.setObjectName("fr_progl")
        self.selVal_8 = QtWidgets.QLabel(self.fr_prog)
        self.selVal_8.setGeometry(QtCore.QRect(0, 50, 20, 20))
        self.selVal_8.setMinimumSize(QtCore.QSize(20, 20))
        self.selVal_8.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selVal_8.setFont(font)
        self.selVal_8.setStyleSheet("background:green;\n"
"color:white;\n"
"")
        self.selVal_8.setAlignment(QtCore.Qt.AlignCenter)
        self.selVal_8.setObjectName("selVal_8")
        self.verticalLayout_4.addWidget(self.fr_prog)
        self.layoutWidget_2 = QtWidgets.QWidget(self.thermometer)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 0, 22, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pmax = QtWidgets.QLabel(self.layoutWidget_2)
        self.pmax.setMinimumSize(QtCore.QSize(0, 16))
        self.pmax.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pmax.setFont(font)
        self.pmax.setStyleSheet("background:green;\n"
" color:white;\n"
"")
        self.pmax.setAlignment(QtCore.Qt.AlignCenter)
        self.pmax.setObjectName("pmax")
        self.verticalLayout_6.addWidget(self.pmax)
        self.pr_prog = QtWidgets.QFrame(self.layoutWidget_2)
        self.pr_prog.setMinimumSize(QtCore.QSize(20, 70))
        self.pr_prog.setMaximumSize(QtCore.QSize(20, 70))
        self.pr_prog.setStyleSheet("background-color: beige;\n"
"border-radius:5px;")
        self.pr_prog.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pr_prog.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pr_prog.setObjectName("pr_prog")
        self.pr_progl = QtWidgets.QLabel(self.pr_prog)
        self.pr_progl.setGeometry(QtCore.QRect(0, 50, 20, 5))
        self.pr_progl.setStyleSheet("background-color:rgb(255, 69, 32);\n"
"color:white;\n"
"font-size:11px;\n"
"")
        self.pr_progl.setText("")
        self.pr_progl.setAlignment(QtCore.Qt.AlignCenter)
        self.pr_progl.setObjectName("pr_progl")
        self.selVal_9 = QtWidgets.QLabel(self.pr_prog)
        self.selVal_9.setGeometry(QtCore.QRect(0, 50, 20, 20))
        self.selVal_9.setMinimumSize(QtCore.QSize(20, 20))
        self.selVal_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selVal_9.setFont(font)
        self.selVal_9.setStyleSheet("background:green;\n"
"color:white;\n"
"")
        self.selVal_9.setAlignment(QtCore.Qt.AlignCenter)
        self.selVal_9.setObjectName("selVal_9")
        self.verticalLayout_6.addWidget(self.pr_prog)
        self.layoutWidget_3 = QtWidgets.QWidget(self.thermometer)
        self.layoutWidget_3.setGeometry(QtCore.QRect(40, 0, 22, 91))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tmax = QtWidgets.QLabel(self.layoutWidget_3)
        self.tmax.setMinimumSize(QtCore.QSize(0, 16))
        self.tmax.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tmax.setFont(font)
        self.tmax.setStyleSheet("background:green;\n"
" color:white;\n"
"")
        self.tmax.setAlignment(QtCore.Qt.AlignCenter)
        self.tmax.setObjectName("tmax")
        self.verticalLayout_8.addWidget(self.tmax)
        self.tv_prog = QtWidgets.QFrame(self.layoutWidget_3)
        self.tv_prog.setMinimumSize(QtCore.QSize(20, 70))
        self.tv_prog.setMaximumSize(QtCore.QSize(20, 70))
        self.tv_prog.setStyleSheet("background-color: beige;\n"
"border-radius:5px;")
        self.tv_prog.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tv_prog.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tv_prog.setObjectName("tv_prog")
        self.tv_progl = QtWidgets.QLabel(self.tv_prog)
        self.tv_progl.setGeometry(QtCore.QRect(0, 50, 20, 5))
        self.tv_progl.setStyleSheet("background-color:rgb(255, 69, 32);\n"
"color:white;\n"
"font-size:11px;\n"
"")
        self.tv_progl.setText("")
        self.tv_progl.setAlignment(QtCore.Qt.AlignCenter)
        self.tv_progl.setObjectName("tv_progl")
        self.selVal_10 = QtWidgets.QLabel(self.tv_prog)
        self.selVal_10.setGeometry(QtCore.QRect(0, 50, 22, 20))
        self.selVal_10.setMinimumSize(QtCore.QSize(20, 20))
        self.selVal_10.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.selVal_10.setFont(font)
        self.selVal_10.setStyleSheet("background:green;\n"
"color:white;\n"
"")
        self.selVal_10.setAlignment(QtCore.Qt.AlignCenter)
        self.selVal_10.setObjectName("selVal_10")
        self.verticalLayout_8.addWidget(self.tv_prog)
        self.verticalLayout_7.addWidget(self.thermometer)
        self.gridLayout_2.addWidget(self.frame_2, 0, 2, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(450, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pGraph = PlotWidget(self.frame)
        self.pGraph.setMinimumSize(QtCore.QSize(0, 100))
        self.pGraph.setStyleSheet("background-color: rgb(255, 47, 130);")
        self.pGraph.setObjectName("pGraph")
        self.gridLayout.addWidget(self.pGraph, 0, 0, 1, 1)
        self.frGraph = PlotWidget(self.frame)
        self.frGraph.setMinimumSize(QtCore.QSize(0, 100))
        self.frGraph.setStyleSheet("background-color: rgb(122, 255, 74);")
        self.frGraph.setObjectName("frGraph")
        self.gridLayout.addWidget(self.frGraph, 1, 0, 1, 1)
        self.ecGraph = PlotWidget(self.frame)
        self.ecGraph.setMinimumSize(QtCore.QSize(0, 100))
        self.ecGraph.setStyleSheet("background-color: rgb(255, 235, 6);")
        self.ecGraph.setObjectName("ecGraph")
        self.gridLayout.addWidget(self.ecGraph, 3, 0, 1, 1)
        self.tvGraph = PlotWidget(self.frame)
        self.tvGraph.setMinimumSize(QtCore.QSize(0, 100))
        self.tvGraph.setStyleSheet("background-color: rgb(255, 70, 153);")
        self.tvGraph.setObjectName("tvGraph")
        self.gridLayout.addWidget(self.tvGraph, 2, 0, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_3.setStyleSheet("")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.setting = QtWidgets.QPushButton(self.frame_3)
        self.setting.setMinimumSize(QtCore.QSize(50, 50))
        self.setting.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/resources/icons8_services_64px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setting.setIcon(icon)
        self.setting.setIconSize(QtCore.QSize(40, 40))
        self.setting.setCheckable(False)
        self.setting.setFlat(True)
        self.setting.setObjectName("setting")
        self.horizontalLayout_8.addWidget(self.setting)
        self.notification = QtWidgets.QFrame(self.frame_3)
        self.notification.setMinimumSize(QtCore.QSize(50, 50))
        self.notification.setMaximumSize(QtCore.QSize(16777215, 50))
        self.notification.setStyleSheet("")
        self.notification.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notification.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notification.setObjectName("notification")
        self.notification_btn = QtWidgets.QPushButton(self.notification)
        self.notification_btn.setGeometry(QtCore.QRect(0, 10, 50, 40))
        self.notification_btn.setStyleSheet("background:transparent;")
        self.notification_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resources/icons8_alarm_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notification_btn.setIcon(icon1)
        self.notification_btn.setIconSize(QtCore.QSize(30, 30))
        self.notification_btn.setFlat(True)
        self.notification_btn.setObjectName("notification_btn")
        self.nc_label = QtWidgets.QLabel(self.notification)
        self.nc_label.setGeometry(QtCore.QRect(25, 0, 25, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.nc_label.setFont(font)
        self.nc_label.setStyleSheet("background-color: rgb(255, 0, 12);\n"
"border-radius:5px;\n"
"color:beige;")
        self.nc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nc_label.setObjectName("nc_label")
        self.horizontalLayout_8.addWidget(self.notification)
        self.emegency = QtWidgets.QPushButton(self.frame_3)
        self.emegency.setMinimumSize(QtCore.QSize(50, 50))
        self.emegency.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/resources/icons8_doctors_bag_96px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emegency.setIcon(icon2)
        self.emegency.setIconSize(QtCore.QSize(40, 40))
        self.emegency.setCheckable(False)
        self.emegency.setFlat(True)
        self.emegency.setObjectName("emegency")
        self.horizontalLayout_8.addWidget(self.emegency)
        self.filter = QtWidgets.QPushButton(self.frame_3)
        self.filter.setMinimumSize(QtCore.QSize(50, 50))
        self.filter.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/resources/icons8_filter_100px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.filter.setIcon(icon3)
        self.filter.setIconSize(QtCore.QSize(40, 40))
        self.filter.setCheckable(False)
        self.filter.setFlat(True)
        self.filter.setObjectName("filter")
        self.horizontalLayout_8.addWidget(self.filter)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.onscreen_notifier = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.onscreen_notifier.setFont(font)
        self.onscreen_notifier.setStyleSheet("color:red;\n"
"font-size:13px;")
        self.onscreen_notifier.setText("")
        self.onscreen_notifier.setAlignment(QtCore.Qt.AlignCenter)
        self.onscreen_notifier.setObjectName("onscreen_notifier")
        self.horizontalLayout_8.addWidget(self.onscreen_notifier)
        spacerItem8 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.startVent = QtWidgets.QPushButton(self.frame_3)
        self.startVent.setMinimumSize(QtCore.QSize(50, 50))
        self.startVent.setMaximumSize(QtCore.QSize(60, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.startVent.setFont(font)
        self.startVent.setStyleSheet("color:beige;\n"
"border-radius:5px;\n"
"  border-width: 2px;\n"
"    border-style: solid;\n"
"    border-color: rgba(61, 203, 244,100);")
        self.startVent.setIconSize(QtCore.QSize(40, 40))
        self.startVent.setCheckable(False)
        self.startVent.setFlat(True)
        self.startVent.setObjectName("startVent")
        self.horizontalLayout_8.addWidget(self.startVent)
        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        Ventilator.setCentralWidget(self.centralwidget)

        self.retranslateUi(Ventilator)
        QtCore.QMetaObject.connectSlotsByName(Ventilator)

    def retranslateUi(self, Ventilator):
        _translate = QtCore.QCoreApplication.translate
        Ventilator.setWindowTitle(_translate("Ventilator", "Ventilator"))
        self.label_14.setText(_translate("Ventilator", "Peep"))
        self.peep_label.setText(_translate("Ventilator", "5"))
        self.label_15.setText(_translate("Ventilator", "Pdelta"))
        self.pressure_label.setText(_translate("Ventilator", "70"))
        self.label_10.setText(_translate("Ventilator", "BR"))
        self.br_label.setText(_translate("Ventilator", "60"))
        self.label_11.setText(_translate("Ventilator", "FR"))
        self.frMax_label.setText(_translate("Ventilator", "80"))
        self.label_5.setText(_translate("Ventilator", "TV_Set"))
        self.tidalVolume_label.setText(_translate("Ventilator", "500"))
        self.label_7.setText(_translate("Ventilator", "TV_Min"))
        self.tidalVolumeMin_label.setText(_translate("Ventilator", "300"))
        self.label_3.setText(_translate("Ventilator", "HBR"))
        self.hbr_label.setText(_translate("Ventilator", "70"))
        self.label_9.setText(_translate("Ventilator", "bpm"))
        self.label_20.setText(_translate("Ventilator", "FeO2"))
        self.feo2_label.setText(_translate("Ventilator", "96%"))
        self.label_29.setText(_translate("Ventilator", "status"))
        self.status.setText(_translate("Ventilator", "Not running"))
        self.label_18.setText(_translate("Ventilator", "P"))
        self.pr.setText(_translate("Ventilator", "999"))
        self.label_22.setText(_translate("Ventilator", "FRR"))
        self.frr.setText(_translate("Ventilator", "99"))
        self.label_27.setText(_translate("Ventilator", "TVR"))
        self.tvr.setText(_translate("Ventilator", "999"))
        self.label_28.setText(_translate("Ventilator", "UNITS"))
        self.label_30.setText(_translate("Ventilator", "Pressure"))
        self.status_2.setText(_translate("Ventilator", "cmH2O"))
        self.label_31.setText(_translate("Ventilator", "flowRate"))
        self.status_3.setText(_translate("Ventilator", "mL/min"))
        self.label_32.setText(_translate("Ventilator", "Volume"))
        self.status_4.setText(_translate("Ventilator", "mL"))
        self.label_33.setText(_translate("Ventilator", "Gauge Indicators"))
        self.fmax.setText(_translate("Ventilator", "99"))
        self.selVal_8.setText(_translate("Ventilator", "fr"))
        self.pmax.setText(_translate("Ventilator", "99"))
        self.selVal_9.setText(_translate("Ventilator", "fr"))
        self.tmax.setText(_translate("Ventilator", "99"))
        self.selVal_10.setText(_translate("Ventilator", "fr"))
        self.nc_label.setText(_translate("Ventilator", "0"))
        self.startVent.setText(_translate("Ventilator", "START"))

from pyqtgraph import PlotWidget
import udvent_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ventilator = QtWidgets.QMainWindow()
    ui = Ui_Ventilator()
    ui.setupUi(Ventilator)
    Ventilator.show()
    sys.exit(app.exec_())

