# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow,message):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(603, 99)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.notification_2 = QtWidgets.QFrame(self.centralwidget)
        self.notification_2.setGeometry(QtCore.QRect(10, 10, 582, 80))
        self.notification_2.setMaximumSize(QtCore.QSize(600, 80))
        self.notification_2.setStyleSheet("background-color:beige")
        self.notification_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notification_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notification_2.setObjectName("notification_2")
        self.msg_2 = QtWidgets.QLabel(self.notification_2)
        self.msg_2.setGeometry(QtCore.QRect(0, 5, 501, 71))
        self.msg_2.setStyleSheet("background-color: rgb(255,255,255);")
        self.msg_2.setObjectName("msg_2")
        self.ackn_2 = QtWidgets.QPushButton(self.notification_2)
        self.ackn_2.setGeometry(QtCore.QRect(510, 15, 51, 51))
        self.ackn_2.setStyleSheet("\n"
"\n"
"QPushButton{\n"
"border:1px solid  rgb(162, 195, 255);\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover:!pressed\n"
"{\n"
"  border: 1px solid red;\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"  background:beige;\n"
"}")
        self.ackn_2.setFlat(False)
        self.ackn_2.setObjectName("ackn_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow,message[0],message[1])
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow,header="Error Title",content="message Content"):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.msg_2.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;color:red\"> {}".format(header)+" !</span></p><p>{}".format(content)+"</p></body></html>"))
        self.ackn_2.setText(_translate("MainWindow", "OK"))

