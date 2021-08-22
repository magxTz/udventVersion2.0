# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:24:03 2020

@author: Magx
"""
import time
from PyQt5.QtCore import pyqtSignal as pys,QThread as task, QTimer
class debug(task):

    def __init__(self):
        super(debug, self).__init__()
        self.message=None
        self.active=True
        self.allowDebug=False


    def run(self):
        self.allowDebug=True
        while self.active and self.message:
            print(self.message)
            self.message=None
        
        
       

    def killTask(self,com):
        if self.allowDebug:
            self.activate=com
            time.sleep(0.5)
            print("Quiting Debug Mode")
        
        
            
    

        
    
