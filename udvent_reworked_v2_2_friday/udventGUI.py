from udvent import *
from settingForm import *
from readDataThread import *
from abnormal_condition_informer import *
from notify import *
import random
import time
import pyqtgraph as pg
import sys
import numpy as np
from numpy import arange, sin, cos, pi
from collections import deque
from PyQt5.QtCore import pyqtSignal as pys
from debugger import debug
import enum

class hardCodedError(enum.Enum):
    STREIGHT_LINE="Not Breathing","Patient does not receive air from the machine,\n 0 flow rate 0 tidal volume"
    EMPTY_COM_PORT="No COM Device detected","Unplugged, Defective device or cable malfunctioning"
    DEBUG_MODE_ACTIVE="Debug Mode Activated","this can affect program execution speed, and perfomance, switch off Debug mode when not in use"
    VALUE_ERROR="Value Error ","The variable(s) received impoper type of data "
    
    
    
class GUI(QtWidgets.QMainWindow,Ui_Ventilator):
    ready=pys()
    def __init__(self,parent=None):
        #self.setAttribute(Qt.WA_TranslucentBackground)
        super(GUI,self).__init__(parent)
        self.setupUi(self);
        self.showGrids(True)
        self.freq=2048
        self.alarmnormal=0
        self.duration=500
        self.notificationList=[]
        self.state=True
        self.debug=False
        self.blinker=False
        self.disable_alarm=True
        ############## NOTIFICATION#########
        self.n_counter=0
        self.reported=False
        
        self.abn_counter=0
        self.fillweight=30
        self.maxdp=10
        
        global userChanged,userDesire,initiated,splot,plot_filled, started
        initiated= False
        started=False
        userChanged= False
        userDesire= True
        splot=False
        
        #off sets for each graph when single plot area activated HII ni muhimu sitak sahau
        global p_offset,fr_offset,tv_offset,ec_offset
        p_offset=0
        fr_offset=0
        tv_offset=0
        ec_offset=0
        
        plot_filled=True;
        pg.setConfigOptions(antialias=True)
        self.setting_obj=settingForm()

        self.pCurve=None
        self.tvCurve=None
        self.ecCurve=None
        self.frCurve=None
        self.customCodes()
        
        #control Variables
        self.pressureMax=100
        self.pressureMin=0
        self.pressure=0
        self.peep=5
        self.breathRate=0
        self.flowRate=0
        self.tidalVolume=0
        
    
    def customCodes(self):
        #pen size and pen color
        self.p_pen=pg.mkPen(color=(255, 255, 0), width=3)
        self.f_pen=pg.mkPen(color=(255, 0, 0), width=3)
        self.t_pen=pg.mkPen(color=(0,255,0), width=3)
        ####################
        self.ecGraph.setBackground((42, 42, 42))
        if self.n_counter<=0:
            self.nc_label.hide()
        self.startVent.clicked.connect(self.startVentilator)
        self.pGraph.setBackground((42, 42, 42))
        self.frGraph.setBackground((42, 42, 42))
        self.tvGraph.setBackground((42, 42, 42))
        self.pCurve=self.pGraph.plot(pen=self.p_pen,fillLevel=0,   brush=(255,255,50,50))
        self.tvCurve=self.tvGraph.plot(pen=self.t_pen,fillLevel=0,   brush=(255,0,0,70))
        self.frCurve=self.frGraph.plot(pen=self.f_pen,fillLevel=0,   brush=(0,255,0,40)) 
        self.setting.clicked.connect(self.settingWindow)
        self.setting_obj.fill_sig.connect(self.plot_Filler)
        self.setting_obj.grid_sig.connect(self.showGrids)
        self.setting_obj.fw_sig.connect(self.fwUpdater)
        self.setting_obj.embbed_sig.connect(self.embbed2_singlePlot)
        self.setting_obj.eg_sig.connect(self.ecg_hide)
        self.setting_obj.p_sig.connect(self.p_hide)
        self.setting_obj.tv_sig.connect(self.tv_hide)
        self.setting_obj.fr_sig.connect(self.f_hide)
        self.setting_obj.pdial_sig.connect(self.receiveData)
        self.setting_obj.peepdial_sig.connect(self.receiveData)
        self.setting_obj.tvdial_sig.connect(self.receiveData)
        self.setting_obj.frSlider_sig.connect(self.receiveData)
        self.setting_obj.brSlider_sig.connect(self.receiveData)

        self.rd=readData()
        self.rd.ser.close()
        self.verbose=debug()
        self.notifier=notificationForm()

        self.py=[0]
        self.fy=[0]
        self.ty=[0]
        self.px=[0]
        self.fx=[0]
        self.tx=[0]
        pg.setConfigOptions(antialias=True)
        self.rd.error.connect(self.showError)
        self.rd.tvr.connect(self.printer)
        self.rd.prr.connect(self.printer)
        self.rd.frr.connect(self.printer)
        self.notification_btn.clicked.connect(self.openNotification)
 
        

  
        
    def receiveData(self,sender_obj,val):
          self.widget=sender_obj
          if self.widget=="pdial":
               self.pressure=val
               self.pressure_label.setText(str(val))
          elif self.widget=="peepdial":
               self.peep=val
               self.peep_label.setText(str(val))
          elif self.widget=="tvdial":
               self.tidalVolume=val
               self.tidalVolume_label.setText(str(val))
          elif self.widget=="frSlider":
               self.flowRate=val
               self.frMax_label.setText(str(val))
          elif self.widget=="brSlider":
               self.breathRate=val
               self.br_label.setText(str(val))
    def find(self,s,ch):
        return[i for i, ltr in enumerate(s) if ltr==ch]

    def extract_msg(self,s,index):
        return s[index[0]+1:index[1]]

    def find_keys(self,val):
        v=self.find(val,"_")
        head_index=v[:2]
        msg_index=v[2:]
        indices=[head_index,msg_index]
        vital_info=[]
        for i in indices:
            vital_info.append(self.extract_msg(val,i))
        return vital_info

    def removeAckn_Error(self,index):
        key=tuple(self.find_keys(index))
        self.notificationList.remove(key)
        self.n_counter-=1
        self.update_counter_label()
        if self.n_counter<1:
            self.nc_label.hide()
            self.disable_alarm=True
        for er in self.notificationList:
            if er[0] =="Not Breathing":
                self.disable_alarm=False
        if self.disable_alarm:
            self.abn_counter=0
            self.unusualCondition(False)
            self.onscreen_notifier.clear()
            self.reported=False
        
                
        
    def openNotification(self):
        if len(self.notificationList)<1:
            self.notifier=notificationForm(.9,[["",""]])
            self.notifier.show()
        elif len(self.notificationList)>=7:
            self.notifier=notificationForm(.9,self.notificationList[:7])
            self.notifier.acknSig.connect(self.removeAckn_Error)
            self.notifier.show()
        else:
            self.notifier=notificationForm(.9,self.notificationList)
            self.notifier.acknSig.connect(self.removeAckn_Error)
            self.notifier.show()
            
            

    def showError(self,data):
        global started
        self.debug=self.setting_obj.debug
        self.notify4error()
        self.notificationList.append(hardCodedError.EMPTY_COM_PORT.value)
        
        started=False
        self.ventOFF()
        if self.debug:
            self.verboseMode(data)
    def notify4error(self):
        self.machineAlarm("ab")
        self.nc_label.show()
        self.n_counter+=1
        self.update_counter_label()

        
    def update_counter_label(self):
        if self.n_counter>9:
            self.nc_label.setText("9+")
        else:
            self.nc_label.setText(str(self.n_counter))

            
    def verboseMode(self,msg):
        self.verbose.message=msg
        self.verbose.start()
        ################# remove this was for testing purpose
    def showw(self):
        print(self.notificationList)
        #####################
    
    

    def printer(self, data):
        self.pGraph.setXRange(0,self.maxdp+.1,padding=0)
        self.tvGraph.setXRange(0,self.maxdp+.1,padding=0)
        self.frGraph.setXRange(0,self.maxdp+.1,padding=0)
        global userChanged,userDesire,initiated,splot
        global p_offset,fr_offset,tv_offset,ec_offset
        if initiated:
            if splot==True:
                    p_offset=7
                    fr_offset=2
                    tv_offset=-3
                    ec_offset=-6
            else:
                    p_offset=0
                    fr_offset=0
                    tv_offset=0
                    ec_offset=0
            #############################
            if self.px[-1]>(self.maxdp-2*self.rd.scale_x):
               self.pCurve.clear()
               self.px=[]
               self.py=[]
               self.px.append(0)
               self.py.append(0)
               
            elif self.tx[-1]>(self.maxdp-2*self.rd.scale_x):
               self.tvCurve.clear()
               self.tx=[]
               self.ty=[]
               self.tx.append(0)
               self.ty.append(0)
            elif self.fx[-1]>(self.maxdp-2*self.rd.scale_x):
               self.frCurve.clear()
               self.fx=[]
               self.fy=[]
               self.fx.append(0)
               self.fy.append(0)
               
           
            


               

            if data[0]=="p":
               
               self.py.append(round(float(data[data.find('%')+1:]),2)+p_offset)
               self.px.append(round(float(data[1:data.find('%')]),2))
               self.gauge_valueUpdater(data[0],self.py[-1])
               self.pCurve.setData(self.px,self.py)
               self.pr.setText(str(self.py[-1]))
               if self.py[-1]==0:
                   self.abn_counter+=1
                   if self.abn_counter>20 and self.reported==False:
                               self.onscreen_notifier.setText("Abnormal breathing interval... ! {}".format(str(int(10-((self.abn_counter)/5)))))
                   
                                
                   if self.abn_counter>50:
                       self.onscreen_notifier.setText("   DANGER !!!  ")
                       if  self.reported==False:
                           self.nc_label.show()
                           self.n_counter+=1
                           self.notificationList.append(hardCodedError.STREIGHT_LINE.value)
                           self.update_counter_label()
                           self.reported=True
                           
                       if self.abn_counter%5==0:
                           self.machineAlarm("ab")
                           self.blinker= not self.blinker
                           self.onscreen_notifier.setText("   DANGER !!!  ")
                           self.onscreen_notifier.clear()
                           self.unusualCondition(self.blinker)
                           
                           if self.debug:
                               print("No air flowing to the partient for more than 1 minute... \n Consider it as Emergency")
                         
               else:
                   self.abn_counter=0
                   self.unusualCondition(False)
                   self.reported=False
                   self.onscreen_notifier.clear()
                   

                   
               if self.fy[-1]>20:
                   self.alarmnormal+=1
                   if self.alarmnormal==1:
                       self.machineAlarm("n")
               elif self.fy[-1]<0:
                   self.alarmnormal=0


            elif data[0]=="t":
              
               self.tx.append(round(float(data[1:data.find('%')]),2))
               self.ty.append(round(float(data[data.find('%')+1:]),2)+tv_offset)
               self.tvCurve.setData(self.tx,self.ty)
               self.tvr.setText(str(self.ty[-1]))
               self.gauge_valueUpdater(data[0],self.ty[-1])
               

            elif data[0]=="f":
               self.fx.append(round(float(data[1:data.find('%')]),2))
               self.fy.append(round(float(data[data.find('%')+1:]),2)+fr_offset)
               self.frCurve.setData(self.fx,self.fy)
               self.gauge_valueUpdater(data[0],self.fy[-1])
               self.frr.setText(str(self.fy[-1]))
               
            self.debug=self.setting_obj.debug
            self.rd.debug=self.setting_obj.debug
            self.verbose.allowDebug=self.debug

            if self.debug:
                
                try:
                   self.verboseMode("tx : "+str(round(self.tx[-1],2))+
                                    " ty : "+str(round(self.ty[-1],2))+"\n"+"fx : "+str(round(self.px[-1],2))+
                                    "    fy : "+str(round(self.fy[-1],2))+"\n"+"px : "+str(round(self.px[-1],2))+
                                    "    py : "+str(round(self.py[-1],2)))
                   
                   

                except Exception as e:
                   self.verboseMode(str(e))
        
            
        elif userChanged:
            self.filler(userDesire,self.fillweight)
            userChanged=False
            initiated=True
        else:
            self.filler(True)
            initiated = True



    def machineAlarm(self,flag="n"):
        if flag=="n":
            self.beepSound(800,100)
        if flag=="ab":
            self.beepSound(self.freq,self.duration)
            

        ###########################
    def beepSound(self,freq=1000,dur=10000):
        self.alarm=informer()
        self.alarm.freq=freq
        self.alarm.dur=dur
        self.alarm.inform=True
        self.alarm.start()
              
        
        
    def startVentilator(self):
        global started
        started = not  started
        if started:
            self.ventON()
        else:
            self.ventOFF()
            
                    
        
    
        
    def ventON(self) :
        self.startVent.setStyleSheet("background:rgba(255,0,0,170);color:beige;border-radius:5px;border-width: 2px;border-style: solid;border-color: rgba(61, 203, 244,100);")
        self.startVent.setText("STOP")
        self.status.setStyleSheet("color:green;border-width: 2px;border-style: solid;border-color: rgba(61, 203, 244,100);")
        self.state=True
        self.status.setText("Running")
        self.rd.activated=self.state
        self.rd.maxdp=self.maxdp
        self.rd.start()
        
    def ventOFF(self) :
        self.state=False
        self.rd.ser.close()
        self.rd.killTask(self.state)
        self.startVent.setStyleSheet("background:rgb(42, 42, 42);color:beige;border-radius:5px;border-width: 2px;border-style: solid;border-color: rgba(61, 203, 244,100);")
        self.startVent.setText("START")
        self.status.setText("Not Running")
        self.status.setStyleSheet("color:rgb(194, 52, 21);border-width: 2px;border-style: solid;border-color: rgba(61, 203, 244,100);")
        
        
        
    def fwUpdater(self,val):
        global userChanged,initiated,plot_filled
        self.fillweight=val
        if splot==False:
            if plot_filled :
                initiated=False
                userChanged = True
                self.filler(True,val)
                userChanged=False
                initiated=True
            else:
                initiated=True
        else:
            initiated=True;
            

        
    def showGrids(self,grid):
        self.ecGraph.showGrid(x=grid, y=grid)
        self.tvGraph.showGrid(x=grid, y=grid)
        self.frGraph.showGrid(x=grid, y=grid)
        self.pGraph.showGrid(x=grid, y=grid)
        


    def plot_Filler(self,sig):
        global plot_filled,userChanged,initiated,userDesire
        if  splot==False:
            if plot_filled!=sig:
                plot_filled=sig
                initiated=False
                userChanged=True
                userDesire=plot_filled
        else:
            initiated=True
        return

              
    def filler(self,state,fw=30):
        self.pGraph.clear()
        self.tvGraph.clear()
        self.frGraph.clear()
        self.ecGraph.clear()

        
        if state:
            self.pCurve=self.pGraph.plot(pen=self.p_pen,fillLevel=0,   brush=(239,204,0,fw))
            self.frCurve=self.frGraph.plot(pen=self.f_pen,fillLevel=0, brush=(0,255,0,fw))
            #self.ecCurve=self.ecGraph.plot(pen='g',fillLevel=0, brush=(0,255,0,fw))
            self.tvCurve=self.tvGraph.plot(pen=self.t_pen,fillLevel=0, brush=(255,0,0,fw))
        else:
            self.pCurve=self.pGraph.plot(pen=self.p_pen,  fillLevel=0,   brush=None)
            self.frCurve=self.frGraph.plot(pen=self.f_pen,fillLevel=0, brush=None)
            #self.ecCurve=self.ecGraph.plot(pen='g',fillLevel=0, brush=None)
            self.tvCurve=self.tvGraph.plot(pen=self.t_pen,fillLevel=0, brush=None)
            
    def embbed2_singlePlot(self,wanna_change):
        global splot
        initiated=False
        if wanna_change:
            splot=True

            #clear all plot areas first
            
            self.pGraph.clear()
            self.tvGraph.clear()
            self.frGraph.clear()
            self.ecGraph.clear()
            
            # Hide all unwanted graphs
            
            self.tvGraph.hide()
            self.ecGraph.hide()
            self.frGraph.hide()
            
            #Re-create the plotting areas
            
            self.pCurve=self.pGraph.plot(pen=self.p_pen,  fillLevel=0,       brush=None)
            self.tvCurve=self.pGraph.plot(pen=self.t_pen,  fillLevel=0,   brush=None)
            self.frCurve=self.pGraph.plot(pen=self.f_pen,  fillLevel=0,   brush=None)
            #self.ecCurve=self.pGraph.plot(pen='r',  fillLevel=0,   brush=None)
            
            
        else:
            
            self.pGraph.clear()
            
            self.pGraph.show()
            self.tvGraph.show()
            self.frGraph.show()
            self.ecGraph.show()
            splot=False
            self.filler(True,self.fillweight)
            #initiated = True
            
            

      

        
    def ecg_hide(self,val):
        if val:
            self.ecGraph.show()
        else:
            self.ecGraph.hide()
    def p_hide(self,val):
        if val:
            self.pGraph.show()
        else:
            self.pGraph.hide()
    def f_hide(self,val):
        if val:
            self.frGraph.show()
        else:
            self.frGraph.hide()
    def tv_hide(self,val):
        if val:
            self.tvGraph.show()
        else:
            self.tvGraph.hide()
        
    def settingWindow(self):
        
        self.setting_obj.show()

        
    def gauge_valueUpdater(self,sent,val):
        widname=self.sender().objectName()
        if sent=="p":
            self.factor=0.3
            self.pr_progl.move(0,(self.pr_prog.frameGeometry().height()-self.factor*val))
            self.pr_progl.setText(str(val))
            self.pmax.setText(str(str(val)))
            self.pr_progl.resize(20,self.factor*val)
            

        if sent=="t":
            self.factor=.3
            self.tv_progl.move(0,(self.tv_prog.frameGeometry().height()-self.factor*val))
            self.tv_progl.setText(str(val))
            self.tmax.setText(str(str(val)))
            self.tv_progl.resize(20,self.factor*val)
            
        if sent=="f":
            self.factor=5
            self.fr_progl.move(0,(self.fr_prog.frameGeometry().height()-self.factor*val))
            self.fr_progl.setText(str(val))
            self.fr_progl.resize(20,self.factor*val)
            self.fmax.setText(str(str(val)))
            ###################
    def unusualCondition(self,error):
        if error :
            self.fr_prog.setStyleSheet("background-color: red;border-radius:5px;")
            self.tv_prog.setStyleSheet("background-color: red;border-radius:5px;")
            self.pr_prog.setStyleSheet("background-color: red;border-radius:5px;")
            
        else :
            self.fr_prog.setStyleSheet("background-color: beige;border-radius:5px;")
            self.tv_prog.setStyleSheet("background-color: beige;border-radius:5px;")
            self.pr_prog.setStyleSheet("background-color: beige;border-radius:5px;")
            
    def killRunningThreads(self):
        self.rd.killTask(False)
        self.debug=False
        self.verbose.killTask(False)
        time.sleep(.4)
        self.debug=False
        
        

def theApp():
  app=QtWidgets.QApplication(sys.argv)
  form=GUI()
  #form.showFullScreen()
  form.show()
  app.aboutToQuit.connect(form.killRunningThreads)
  
  sys.exit(app.exec_())


if __name__=="__main__":
  theApp()

    
    

   
