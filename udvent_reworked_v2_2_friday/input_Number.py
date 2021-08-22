from userinput import *
from types import SimpleNamespace
import sys
from PyQt5.QtCore import pyqtSignal as pys

class numberInput(QtWidgets.QMainWindow,Ui_MainWindow):
     input_num=pys(str)
     def __init__(self,opacity=1,loc=(200,200),parent=None):
        super(numberInput,self).__init__(parent)
        self.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.btn=SimpleNamespace(name="",text="")
        self.setTransparency(opacity)
        self.input_text=""
        self.close_btn.clicked.connect(self.close)
        self.move(loc[0],loc[1])
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.b1.clicked.connect(self.getNumbers)
        self.b2.clicked.connect(self.getNumbers)
        self.b3.clicked.connect(self.getNumbers)
        self.b4.clicked.connect(self.getNumbers)
        self.b5.clicked.connect(self.getNumbers)
        self.b6.clicked.connect(self.getNumbers)
        self.b7.clicked.connect(self.getNumbers)
        self.b8.clicked.connect(self.getNumbers)
        self.b9.clicked.connect(self.getNumbers)
        self.b0.clicked.connect(self.getNumbers)
        self.ok.clicked.connect(self.submit_inputs)
        self.clr.clicked.connect(self.clear_text)
        self.del_btn.clicked.connect(self.delete_text)
        

     
     
     def getNumbers(self):
         self.btn.name=self.sender().objectName()
         self.btn.text=self.sender().text()
         self.input_text+=self.btn.text
         self.display.setText(self.input_text)
     def delete_text(self):
         self.input_text=self.input_text[:-1]
         self.display.setText(self.input_text)

     def clear_text(self):
         self.display.clear()
         self.input_text=""
     def submit_inputs(self):
         self.input_num.emit(self.input_text)
         self.close()
         
         
 

     def setTransparency(self,pos):
           self.setWindowOpacity(pos)
    





      
          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    numInput=numberInput()
    numInput.setWindowFlags(QtCore.Qt.FramelessWindowHint)
    numInput.show()
    sys.exit(app.exec_())
