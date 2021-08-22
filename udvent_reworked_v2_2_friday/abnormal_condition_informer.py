import winsound as buzzer
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 00:24:03 2020

@author: Magx
"""
from PyQt5.QtCore import pyqtSignal as pys,QThread as task
class informer(task):

    def __init__(self):
        self.freq=None
        self.dur=None
        super(informer, self).__init__()
        self.inform=False
        


    def run(self):
        if self.inform:
            buzzer.Beep(self.freq,self.dur)
            self.inform=False
        
        
        
            
    

        
    
