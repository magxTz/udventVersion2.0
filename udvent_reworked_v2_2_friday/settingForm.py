from setting import *
from msg_box_class import *
from input_Number import  *
from PyQt5.QtCore import pyqtSignal as pys
import sys
class settingForm(QtWidgets.QMainWindow,Ui_setting):
     fill_sig=pys(bool)
     grid_sig=pys(bool)
     fw_sig=pys(int)
     embbed_sig=pys(bool)
     eg_sig=pys(bool)
     p_sig=pys(bool)
     tv_sig=pys(bool)
     fr_sig=pys(bool)
     pdial_sig=pys(str,int)
     peepdial_sig=pys(str,int)
     tvdial_sig=pys(str,int)
     brSlider_sig=pys(str,int)
     frSlider_sig=pys(str,int)
     
     def __init__(self,parent=None):
     
        super(settingForm,self).__init__(parent)
        self.setupUi(self)
        
        global tgState
        self.maxOpacity=1
        self.minOpacity=0.2
        tgState=True
        self.debug=False
        self.mouse_location=(0,0)
        self.grid=True
        self.valueRequesting_obj=""
        

        #############################################################################################
        if tgState:                                                                                 #
            self.tg.move(40,0)                                                                      #
            self.tg.setText(str(1))                                                                 #
            self.tg.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;")       #
            self.toggleSwitch.setStyleSheet("background-color:green;border-radius:10px;")
            
        if self.grid:
            self.tg_g.move(20,0)                                                                    #
            self.tg_g.setText(str(1))                                                               #
            self.tg_g.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;")     #
            self.toggleSwitch_grid.setStyleSheet("background-color:green;border-radius:10px;")      # 
        #############################################################################################
        self.setTransparency(self.trans_slider.value())
        self.eg.toggled[bool].connect(self.hide_ecg)
        self.trans_slider.setMinimum(20)
        self.trans_slider.setMaximum(100)
        self.trans_slider.setValue(60)
        self.pg.toggled[bool].connect(self.hide_p)
        self.frg.toggled[bool].connect(self.hide_fr)
        self.tvg.toggled[bool].connect(self.hide_tv)
        self.fwSlider.valueChanged[int].connect(self.fillLevelUpdater)
        self.embbed.clicked.connect(self.embbed_rd)
        self.separate.clicked.connect(self.isolate_rd)
        self.tg.clicked.connect(self.toggle)
        self.tg_btn.clicked.connect(self.toggle)
        self.tg_g.clicked.connect(self.toggle)
        self.trans_slider.valueChanged[int].connect(self.setTransparency)
        self.pdial.valueChanged.connect(self.sendValues)
        self.tvdial.valueChanged.connect(self.sendValues)
        self.peepdial.valueChanged.connect(self.sendValues)
        self.frSlider.valueChanged.connect(self.sendValues)
        self.brSlider.valueChanged.connect(self.sendValues)
        self.pdValue.clicked.connect(self.openNI_window)
        self.peepValue.clicked.connect(self.openNI_window)
        self.tvValue.clicked.connect(self.openNI_window)
        self.frValue.clicked.connect(self.openNI_window)
        self.brValue.clicked.connect(self.openNI_window)
        
        

     def openNI_window(self):
          self.valueRequesting_obj=self.sender().objectName()
          self.mouse_location=(self.pos().x(),self.sender().pos().y()+self.pos().y())
          self.numericInput_window=numberInput(loc=self.mouse_location)
          self.numericInput_window.input_num.connect(self.receivedData)
          self.numericInput_window.show()

     def receivedData(self,data):
          self.requesting_obj=self.findChild(QtWidgets.QLabel,self.valueRequesting_obj)
          if self.valueRequesting_obj=="pdValue":
               if(int(data)>self.pdial.maximum()):
                    error="Error","The value of pressure can not exceed <b>{}</b> ".format(str(self.pdial.maximum()))+"<br>please repeat the process "
                    self.alert=msg_box(msg=error)
                    self.alert.show()
               else:
                    self.requesting_obj.setText(data)
                    self.pdial_sig.emit("pdial",int(data))
                    self.pdial.setValue(int(data))
                    self.valueRequesting_obj=""
          elif self.valueRequesting_obj=="peepValue":
               if(int(data)>self.peepdial.maximum()):
                    error="Error","The value of PEEP can not exceed <b>{}</b> ".format(str(self.peepdial.maximum()))+"<br>please repeat the process "
                    self.alert=msg_box(msg=error)
                    self.alert.show()
               else:
                    self.requesting_obj.setText(data)
                    self.peepdial_sig.emit("peepdial",int(data))
                    self.peepdial.setValue(int(data))
                    self.valueRequesting_obj=""
          elif self.valueRequesting_obj=="tvValue":
               if(int(data)>self.tvdial.maximum()):
                    error="Error","The value of Tidal Volume can not exceed <b>{}</b> ".format(str(self.tvdial.maximum()))+"<br>please repeat the process "
                    self.alert=msg_box(msg=error)
                    self.alert.show()
               else:
                    self.requesting_obj.setText(data)
                    self.tvdial_sig.emit("tvdial",int(data))
                    self.tvdial.setValue(int(data))
                    self.valueRequesting_obj=""
          elif self.valueRequesting_obj=="frValue":
               if(int(data)>self.frSlider.maximum()):
                    error="Error","The value of flow Rate can not exceed <b>{}</b> ".format(str(self.frSlider.maximum()))+"<br>please repeat the process "
                    self.alert=msg_box(msg=error)
                    self.alert.show()
               else:
                    self.requesting_obj.setText(data)
                    self.frSlider_sig.emit("frSlider",int(data))
                    self.frSlider.setValue(int(data))
                    self.valueRequesting_obj=""
          elif self.valueRequesting_obj=="brValue":
               if(int(data)>self.brSlider.maximum()):
                    error="Error","The value of Breath Rate can not exceed <b>{}</b> ".format(str(self.brSlider.maximum()))+"<br>please repeat the process "
                    self.alert=msg_box(msg=error)
                    self.alert.show()
               else:
                    self.requesting_obj.setText(data)
                    self.brSlider_sig.emit("brSlider",int(data))
                    self.brSlider.setValue(int(data))
                    self.valueRequesting_obj=""
       
          



##     def mousePressEvent(self,QMouseEvent):
##          cursor=QtGui.QCursor()
##          self.mouse_location=cursor.pos()
##          print(self.mouse_location)
          
##     def mousePressEvent(self,QMouseEvent):
##          print(QMouseEvent.pos())
          
     def sendValues(self,val):
          self.widget=self.sender().objectName()
          if self.widget=="pdial":
               self.pdial_sig.emit(self.widget,val)
          elif self.widget=="peepdial":
               self.peepdial_sig.emit(self.widget,val)
          elif self.widget=="tvdial":
               self.tvdial_sig.emit(self.widget,val)
          elif self.widget=="frSlider":
               self.frSlider_sig.emit(self.widget,val)
          elif self.widget=="brSlider":
               self.brSlider_sig.emit(self.widget,val)
          
     def setTransparency(self,pos):
          trans=pos*(self.maxOpacity-self.minOpacity)/(self.trans_slider.maximum()-self.trans_slider.minimum())
          self.setWindowOpacity(trans)
          
     def hide_ecg(self,val):
        self.eg_sig.emit(val)
    
     def hide_tv(self,val):
        self.tv_sig.emit(val)
    
     def hide_fr(self,val):
        self.fr_sig.emit(val)
    
     def hide_p(self,val):
        self.p_sig.emit(val)
        
     def fill_rd(self):
          self.fill_sig.emit(True)
     
     def unfill_rd(self):
          self.fill_sig.emit(False)
          
     def embbed_rd(self):
          self.embbed_sig.emit(True)
          
     def isolate_rd(self):
          self.embbed_sig.emit(False)
          
         
     def fillLevelUpdater(self, value):
         self.fw_sig.emit(value)

     def toggle(self):
          self.sent=self.sender().objectName()
          if self.sent=="tg":
               global tgState
               tgState=not tgState;
               self.fill_sig.emit(tgState)
               if tgState:
                      self.tg.move(40,0)
                      self.tg.setText(str(1))
                      self.tg.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;")
                      self.toggleSwitch.setStyleSheet("background-color:green;border-radius:10px;")
               else:
                      self.tg.move(0,0)
                      self.tg.setText(str(0))
                      self.tg.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;color:red;")
                      self.toggleSwitch.setStyleSheet("background-color:red;border-radius:10px;")
                      
          if self.sent=="tg_btn":
               self.debug= not self.debug
               if self.debug:
                      self.tg_btn.move(40,0)
                      self.tg_btn.setText(str(1))
                      self.tg_btn.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;")
                      self.debug_tg.setStyleSheet("background-color:green;border-radius:10px;")
               else:
                      self.tg_btn.move(0,0)
                      self.tg_btn.setText(str(0))
                      self.tg_btn.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;color:red;")
                      self.debug_tg.setStyleSheet("background-color:red;border-radius:10px;")
          if self.sent=="tg_g":
               self.grid= not self.grid
               self.grid_sig.emit(self.grid)
               if self.grid:
                      self.tg_g.move(20,0)
                      self.tg_g.setText(str(1))
                      self.tg_g.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;")
                      self.toggleSwitch_grid.setStyleSheet("background-color:green;border-radius:10px;")
               else:
                      self.tg_g.move(0,0)
                      self.tg_g.setText(str(0))
                      self.tg_g.setStyleSheet("background-color: rgb(248, 248, 248);border-radius:10px;color:red;")
                      self.toggleSwitch_grid.setStyleSheet("background-color:red;border-radius:10px;")
  
     
          

def main():
    app=QtWidgets.QApplication(sys.argv)
    form=settingForm()
    form.show()
    sys.exit(app.exec_())
if __name__=="__main__":
    main()



        
        
