# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:03:26 2018

@author: Arlo Eardley 1108472
"""
import socket

#Create the TCP socket
TCPsocket = socket.socket()

#Connect to local host on port 7000
TCPsocket.connect(('127.0.0.1',7000))

#Accept user input as mesage to send to server
Message = raw_input("Message from client: ")

#Send the message to the server
TCPsocket.send(Message.encode("UTF-8"))

#Close the socket 
TCPsocket.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    