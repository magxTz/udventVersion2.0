
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal as pys

class Ui_MainWindow(object):
    acknSig=pys(str)
    def setupUi(self, MainWindow,error_container):
        self.mainwindow=MainWindow
        self.count=len(error_container)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 105)
        MainWindow.setMinimumSize(QtCore.QSize(440,500))
        MainWindow.setMaximumSize(QtCore.QSize(440, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        if self.count>0:
            for i in range(self.count):
                if error_container[0]==["",""]:
                    str1="No Error Reported"
                    str2="Everything is running Fine"
                    error_container=[str1,str2]
                    self.create_notification(error_container,i,btn=False)
                else:
                    self.create_notification(error_container[i],i)
                    self.ackn.clicked.connect(self.acknowledge)
                    





        
    def create_notification(self,err,item_num=0,btn=True):
        self.notification = QtWidgets.QFrame(self.centralwidget)
        self.notification.setMaximumSize(QtCore.QSize(420, 80))
        self.notification.setStyleSheet("background-color:beige;")
        self.notification.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.notification.setFrameShadow(QtWidgets.QFrame.Raised)
        self.notification.setObjectName("notification_"+str(item_num+1))
        self.msg = QtWidgets.QLabel(self.notification)
        self.msg.setGeometry(QtCore.QRect(0, 5, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.msg.setFont(font)
        self.msg.setStyleSheet("background-color: rgb(255,255,255);")
        self.msg.setObjectName("msg_{}"+str(item_num+1))
        self.ackn = QtWidgets.QPushButton(self.notification)
        self.ackn.setGeometry(QtCore.QRect(390, 30, 30, 30))
        self.ackn.setStyleSheet("\n"
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
        self.ackn.setFlat(False)
        if btn==False:
            self.ackn.setVisible(False)
        self.ackn.setObjectName("ackn_{}"+str(item_num+1))
        self.verticalLayout.addWidget(self.notification)
        self.mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.mainwindow,err[0],err[1])
        QtCore.QMetaObject.connectSlotsByName(self.mainwindow)


    def retranslateUi(self, MainWindow,header="Error Title",msg="message Content"):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.msg.setText(_translate("MainWindow","<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;color:red\"> _{}_".format(header)+" ! "+
                                    "</span></p><p>_{}_".format(msg)+"</p></body></html>"))
        self.ackn.setText(_translate("MainWindow", "OK"))

        
    def acknowledge(self):
        try:
            self.sent=self.sender().objectName()
            self.acknSig.emit(self.msg.text())
            name="notification_{}".format(self.sent[-1])
            self.found=self.findChild(QtWidgets.QFrame,name)
            self.found.hide()
    
            
        except Exception as e:
            print(str(e))




