from messagebox import *
from types import SimpleNamespace
import sys
from PyQt5.QtCore import pyqtSignal as pys

class msg_box(QtWidgets.QMainWindow,Ui_MainWindow):
     input_num=pys(str)
     def __init__(self,opacity=1,loc=(200,200),msg=["",""],parent=None):
        super(msg_box,self).__init__(parent)
        self.message=msg
        self.setupUi(self,self.message)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ackn_2.clicked.connect(self.close)

      
          
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form=msg_box()
    form.show()
    sys.exit(app.exec_())
