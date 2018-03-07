# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:03:26 2018

@author: Arlo Eardley 1108472
"""
import socket

#Create teh TCP socket
TCPsocket = socket.socket()

#Connect to the local host on port 7000
TCPsocket.connect(('127.0.0.1',7000))

#Accept user input for the message to send to the server
Message = raw_input("Message from client: ")


#While the client has not selected to quit
while Message != 'q':
    
    #Send a message to the server
    TCPsocket.send(Message.encode("UTF-8"))
    
    #Receive the reply from teh server
    ReceivedData = TCPsocket.recv(4096).decode("UTF-8")
    
    #Print the reply 
    print ('Received from server: ' + ReceivedData)
    
    #Type a new message to send to server 
    Message = raw_input("Message from client: ")
    
    
#Close the connection
TCPsocket.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    