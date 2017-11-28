# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:47:05 2017

@author: Work
"""
# The code for changing pages was derived from:
# http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
# License: http://creativecommons.org/licenses/by-sa/3.0/	
# Edited By Anthony Mukuka Mwila for Final Year Project 2017
# Electrical Engineering Stellenbosch University 
import Tkinter as tk
import socket
import sys
import time;
import random ;


Log_File = open("BLM Counts", "a+")
LARGE_FONT= ("Verdana", 12)

# Definition of ReadCounts Function used to initiate request for BLM Count Data
# from STM32F7 Microcontoller the code was derived from a python client example obtained
# from ............

def  ReadCounts():
    # Host IP Address as defined by DHCP Configuration 
    host = '192.168.1.2'
    # TCP port arbitrarily selected by author 
    port = 50000
    # Python Socket connection code 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print('Failed to create socket')
        sys.exit()

    print('# Getting remote IP address') 
    try:
        remote_ip = socket.gethostbyname( host )
    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()
 
    # Connect to remote server
    print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
    s.connect((remote_ip , port))
 
    # Send data to remote server
    print('# Sending data to server')
    request = "GET / HTTP/1.0\r\n\r\n"
 
    try:
        s.sendall(request.encode())
    except socket.error:
        print ('Send failed')
        sys.exit()
 
    # Receive data
    print('# Receive data from server')
    reply = s.recv(4096)
    localtime = time.asctime(time.localtime(time.time()))
     # Code to genrate random numbers to mimic BLM counts
     a = random.randint(0, 5000);
     b = random.randint(0, 5000);
     #print( localtime,'; Count A is', a ,';Count B is',b);
     log = str(localtime) +'; Count A is '+ str(a) +';Count B is ' + str(b);
     #print(log)
     loga = '\n Count A is '+ str(a) +'\n Count B is ' + str(b)
     Log_File.write(loga)
     #print (reply)
     Log_File.close
    
# Class of Code     
class BLM_PC_Software(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="MENU", font=LARGE_FONT)
        label.pack(pady=100,padx=100)

        button = tk.Button(self, text="CURRENT COUNT",
                            command=lambda: controller.show_frame(PageOne))
        button.pack()

        button2 = tk.Button(self, text="LIVE MODE",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="CURRENT COUNT", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to MENU",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="LIVE MODE",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()
        
        
        button3 = tk.Button(self, text="ReadCounts",
                            command = ReadCounts)
        button3.pack()



class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="LIVE MODE", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to MENU",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="CURRENT COUNT",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        
        button3 = tk.Button(self, text="ReadCounts",
                            command= ReadCounts)
        button3.pack()

app = BLM_PC_Software()
app.mainloop()


