# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 14:55:25 2017

@author: Anthony Mukuka Mwila 
"""

# Importing Required 
import tkinter as tk 
#import tkMessageBox
import socket
import sys

Log_File = open("BLM Counts", "a")

def  ReadCounts():
    
#    host = '192.168.1.2'
#    port = 50000
#    try:
#        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#    except socket.error:
#        print('Failed to create socket')
#        sys.exit()
#
#    print('# Getting remote IP address') 
#    try:
#        remote_ip = socket.gethostbyname( host )
#    except socket.gaierror:
#        print('Hostname could not be resolved. Exiting')
#        sys.exit()
# 
#    # Connect to remote server
#    print('# Connecting to server, ' + host + ' (' + remote_ip + ')')
#    s.connect((remote_ip , port))
# 
#    # Send data to remote server
#    print('# Sending data to server')
#    request = "GET / HTTP/1.0\r\n\r\n"
# 
#    try:
#        s.sendall(request.encode())
#    except socket.error:
#        print ('Send failed')
#        sys.exit()
# 
#    # Receive data
#    print('# Receive data from server')
    reply = 'Yeah'
    Log_File.write(reply)
    
    
#Initialisation of GUI 
MyDisplay = tk.Tk()
MyDisplay.title('BLM Pulse Counter Demo Gui')
MyDisplay.geometry('450x450+500+300')

Channel_A_Label = tk.Label(text ='Channel A')
Channel_A_Label.place(x =25 , y = 25)

Channel_B_Label = tk.Label(text ='Channel B').place(x = 350 , y= 25)

Update_Histogram_A = tk.Button(text= 'Read and Log Counts',command = ReadCounts).place(x = 40 , y = 300)
Update_Histogram_B = tk.Button(text= 'Update B').place(x = 350, y = 300)                       



MyDisplay.mainloop()


                      
                      
                      
                      

                      
    
