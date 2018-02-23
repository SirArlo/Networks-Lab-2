# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:03:26 2018

@author: eards
"""
import socket


TCPsocket = socket.socket()
TCPsocket.connect(('127.0.0.1',7000))
Message = raw_input("Message from client: ")

while Message != 'q':
    TCPsocket.send(Message.encode("UTF-8"))
    ReceivedData = TCPsocket.recv(4096).decode("UTF-8")
    print ('Received from server: ' + ReceivedData)
    Message = raw_input("Message from client: ")
    
TCPsocket.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    