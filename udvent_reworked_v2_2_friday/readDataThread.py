# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:24:03 2020

@author: Magx
"""

from PyQt5.QtCore import pyqtSignal as pys,QThread as task, QTimer
import time
import random
import serial

class readData(task):
    error = pys(str)
    prr=pys(str)
    tvr=pys(str)
    frr=pys(str)
    ecgr=pys(str)
    def __init__(self,parent=None):
        super(readData, self).__init__(parent)
        self.activated=True
        self.scale_x=0.05
        self.debug=False
        self.ser = serial.Serial()
        self.maxdp=20
        self.x_dp=0

    ###########################
    def run(self):
        try:
            #ser=serial.Serial('/dev/ttyACM0',115200,timeout=1)
            self.ser = serial.Serial("COM20", 115200,timeout=1)
            if self.ser.isOpen():
                self.ser.close()
                state="closed" if not self.ser.isOpen() else "open"
                if self.debug:
                    print("Closing serial port.... : "+state)
                self.ser.open()
                state="closed" if not self.ser.isOpen() else "open"
                if self.debug:
                    print("now openning... : "+state)
                    print("connected to: " + self.ser.portstr)


            else:
                self.ser.open()
            while self.activated:
                #while self.ser.in_waiting:  # Or: while ser.inWaiting():
                if self.ser.in_waiting>0:
                    data=str(self.ser.readline().rstrip(),'utf-8')
                    v=data.split(",")
                    for val in v:
                        inserted=str(round(self.x_dp,2)) +"%"
                        val=self.insert(val,inserted,1)
                        self.upd(val)
                    self.x_dp+=self.scale_x#with the function that reads value from our mcu
                    time.sleep(0.05)
                    if self.x_dp>=self.maxdp:
                        self.x_dp=0
                    #time.sleep(0.001)
                

        except Exception as e:
            self.error.emit(str(e))
            #time.sleep(.1)

        
    def upd(self,data):
        if data[0]=="f":
            self.frr.emit(str(data))
        elif data[0]=="t":
            self.tvr.emit(str(data))
        elif data[0]=="p":
            self.prr.emit(str(data))
    def insert (self,source, value, pos):
        return source[:pos]+value+source[pos:]
        
    ######################

    def killTask(self,com):
        self.activated=com
        time.sleep(0.1)
        if self.debug:
            print("thread Killed")
        
            
    

        
    
