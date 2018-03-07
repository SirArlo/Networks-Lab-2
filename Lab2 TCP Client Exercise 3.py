# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:03:26 2018

@author: Arlo Eardley 1108472
"""
import socket

#Create the TCP server
TCPsocket = socket.socket()

#Connect to the local host 
TCPsocket.connect(('127.0.0.1',7000))

#Accept user input to send to server
Message = raw_input("Message from client: ")


#While the client has not ellected to quit
while Message != 'q':
    
    #Send a message to the server
    TCPsocket.send(Message.encode("UTF-8"))
    
    #Receive the data from the server
    ReceivedData = TCPsocket.recv(4096).decode("UTF-8")
    
    #Print out the message from the server
    print ('Received from server: ' + ReceivedData)
    
    #accept a new message from the client to the server
    Message = raw_input("Message from client: ")


#Close the connction
TCPsocket.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    