# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 12:12:25 2017

@author: Work
"""
# Socket client example in python
 
import socket
import sys

host = '192.168.1.2'
port = 50000  
 
# create socket
print('# Creating socket')
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
 
print (reply)
