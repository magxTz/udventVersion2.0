from notifyForm import *
import sys
from PyQt5.QtCore import pyqtSignal as pys
class notificationForm(QtWidgets.QMainWindow,Ui_MainWindow):
     closing=pys(str)
     def __init__(self,opacity=1,err=[["",""]],parent=None):
        super(notificationForm,self).__init__(parent)
        self.error=err
        self.setupUi(self,self.error)
        self.setTransparency(opacity)


     def setTransparency(self,pos):
           self.setWindowOpacity(pos)
     def closingProcedure(self):
          self.closing.emit("closing")

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    form=notificationForm()
    form.show()
    app.aboutToQuit.connect(form.closingProcedure)
    sys.exit(app.exec_())
    
    


      
          
