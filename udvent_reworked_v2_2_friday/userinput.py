# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(150, 191)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QPushButton{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(193, 124, 53,220);\n"
"border:1px solid beige;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(219, 175, 131);\n"
"border:1px solid beige;\n"
"}\n"
"\n"
"QPushButton#ok{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(44, 44, 44,220);\n"
"border: 1px solid beige;\n"
"}\n"
"QPushButton#ok:hover{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(44, 44, 44,100);\n"
"border: 2px solid beige;\n"
"border:1px solid rgb( 219, 175, 131 );\n"
"\n"
"}\n"
"QPushButton#clr{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(219, 175, 131,220);\n"
"border: 1px solid beige;\n"
"}\n"
"\n"
"QPushButton#clr:hover{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(219, 175, 131);\n"
"border: 1px solid beige;\n"
"}\n"
"\n"
"QPushButton#del{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(152, 125, 98,220);\n"
"border: 1px solid beige;\n"
"}\n"
"QPushButton#del:hover{\n"
"border-radius:10px;\n"
"color:white;\n"
"background-color: rgb(152, 125, 98,100);\n"
"border:1px solid beige;\n"
"}\n"
"\n"
"*{\n"
"background-color: rgb(44, 44, 44, 150);\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.display = QtWidgets.QLabel(self.centralwidget)
        self.display.setMinimumSize(QtCore.QSize(100, 40))
        self.display.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.display.setFont(font)
        self.display.setStyleSheet("color:beige;")
        self.display.setText("")
        self.display.setAlignment(QtCore.Qt.AlignCenter)
        self.display.setObjectName("display")
        self.horizontalLayout.addWidget(self.display)
        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.close_btn.setMaximumSize(QtCore.QSize(30, 30))
        self.close_btn.setStyleSheet("background-color: rgb(44, 44, 44);")
        self.close_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons8_delete_48px.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_btn.setIcon(icon)
        self.close_btn.setFlat(True)
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setMinimumSize(QtCore.QSize(30, 30))
        self.b1.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setObjectName("b1")
        self.gridLayout.addWidget(self.b1, 0, 0, 1, 1)
        self.ok = QtWidgets.QPushButton(self.centralwidget)
        self.ok.setMinimumSize(QtCore.QSize(30, 30))
        self.ok.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.gridLayout.addWidget(self.ok, 2, 3, 1, 1)
        self.del_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_btn.setMinimumSize(QtCore.QSize(30, 30))
        self.del_btn.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(True)
        font.setWeight(75)
        self.del_btn.setFont(font)
        self.del_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons8_clear_symbol_50px_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_btn.setIcon(icon1)
        self.del_btn.setFlat(True)
        self.del_btn.setObjectName("del_btn")
        self.gridLayout.addWidget(self.del_btn, 0, 3, 1, 1)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setMinimumSize(QtCore.QSize(30, 30))
        self.b2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.gridLayout.addWidget(self.b2, 0, 1, 1, 1)
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setMinimumSize(QtCore.QSize(30, 30))
        self.b7.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b7.setFont(font)
        self.b7.setObjectName("b7")
        self.gridLayout.addWidget(self.b7, 2, 0, 1, 1)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setMinimumSize(QtCore.QSize(30, 30))
        self.b5.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b5.setFont(font)
        self.b5.setObjectName("b5")
        self.gridLayout.addWidget(self.b5, 1, 1, 1, 1)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setMinimumSize(QtCore.QSize(30, 30))
        self.b6.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b6.setFont(font)
        self.b6.setObjectName("b6")
        self.gridLayout.addWidget(self.b6, 1, 2, 1, 1)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setMinimumSize(QtCore.QSize(30, 30))
        self.b3.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setObjectName("b3")
        self.gridLayout.addWidget(self.b3, 0, 2, 1, 1)
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setMinimumSize(QtCore.QSize(30, 30))
        self.b4.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setObjectName("b4")
        self.gridLayout.addWidget(self.b4, 1, 0, 1, 1)
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setMinimumSize(QtCore.QSize(30, 30))
        self.b8.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b8.setFont(font)
        self.b8.setObjectName("b8")
        self.gridLayout.addWidget(self.b8, 2, 1, 1, 1)
        self.clr = QtWidgets.QPushButton(self.centralwidget)
        self.clr.setMinimumSize(QtCore.QSize(30, 30))
        self.clr.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.clr.setFont(font)
        self.clr.setObjectName("clr")
        self.gridLayout.addWidget(self.clr, 1, 3, 1, 1)
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setMinimumSize(QtCore.QSize(30, 30))
        self.b9.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b9.setFont(font)
        self.b9.setObjectName("b9")
        self.gridLayout.addWidget(self.b9, 2, 2, 1, 1)
        self.b0 = QtWidgets.QPushButton(self.centralwidget)
        self.b0.setMinimumSize(QtCore.QSize(30, 30))
        self.b0.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.b0.setFont(font)
        self.b0.setObjectName("b0")
        self.gridLayout.addWidget(self.b0, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.b1.setText(_translate("MainWindow", "1"))
        self.ok.setText(_translate("MainWindow", "OK"))
        self.b2.setText(_translate("MainWindow", "2"))
        self.b7.setText(_translate("MainWindow", "7"))
        self.b5.setText(_translate("MainWindow", "5"))
        self.b6.setText(_translate("MainWindow", "6"))
        self.b3.setText(_translate("MainWindow", "3"))
        self.b4.setText(_translate("MainWindow", "4"))
        self.b8.setText(_translate("MainWindow", "8"))
        self.clr.setText(_translate("MainWindow", "clr"))
        self.b9.setText(_translate("MainWindow", "9"))
        self.b0.setText(_translate("MainWindow", "0"))

import user_qrc_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

