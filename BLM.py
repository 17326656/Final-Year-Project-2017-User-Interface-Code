# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:25:05 2017

@author: Work
"""

import tkinter as tk




class BLMPulseCounter(tk.Tk):
        
    def _init_(self,*args,**kwargs):
        tk.Tk._init_(self , *args , **kwargs)
        container = tk.Frame(self)
        
        container.pack(side="top" , fill ="both" , expand = True)
        
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0,weight = 1)
        
        self.frames = {}
        
        frame = StartPage(container , self )
        
        self.frames[StartPage] = frame
                   
        frame.grid(row=0 , column = 0 , sticky = "nsew")
                   
        self.show_frame(StartPage)
        
        
    def show_frame(self , cont):
        
        frame = self.frames[cont]
        frame.tkraise()
        
        
        
class StartPage(tk.Frame):
      
    def _init_(self , parent , controller):
        tk.Frame._init_(self , parent)
        label = tk.Label(self , text = "Start Page" )
        label.place(x= 0,y = 0);
        
        
 


       
app = BLMPulseCounter()
app.mainloop()