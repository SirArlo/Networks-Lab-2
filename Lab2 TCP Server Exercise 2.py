# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:57 2018

@author: Arlo Eardley 1108472
"""
import socket

#Create a TCP socket 
TCPsocket =socket.socket()

#Bind to the local host
TCPsocket.bind(('127.0.0.1', 7000)) 

#isten for up to 5 connections
TCPsocket.listen(5)

#Accept the connection from the client
connection, address = TCPsocket.accept() 


#Print out where the connection request has come from
print ("Connection request from address: " + str(address))

#While the client is still sending data
while 1:
    
    #Receive data from the client
    ReceivedFromClient = connection.recv(4096).decode("UTF-8")
    
    #If not data is received the client has disconnected
    if not ReceivedFromClient:
        break
    
    #Print the message received from the client
    print(ReceivedFromClient)
    
    #Echo the client message back to the client
    connection.send(ReceivedFromClient.encode("UTF-8")) 
    

#Close the TCP server
connection.close()
    
   