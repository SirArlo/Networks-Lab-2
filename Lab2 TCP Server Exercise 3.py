# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:57 2018

@author: eards
"""
import socket

#Create the TCP socket
TCPsocket =socket.socket()

#Bind the connection to the local host
TCPsocket.bind(('127.0.0.1', 7000))

#Listen for up to five connections
TCPsocket.listen(5)

#Accept the connection request from the client
connection, address = TCPsocket.accept()

#Print out where the connection has come from
print ("Connection request from address: " + str(address))

#While teh client is still connected
while 1:
    
    #Receive data from the client
    ReceivedFromClient = connection.recv(4096).decode("UTF-8")
    
    #If no data is received then teh client has disconnected
    if not ReceivedFromClient:
        break
    
    #Print out the message from the client
    print(ReceivedFromClient) 
    
    #Allow the server to respond with user input
    response = raw_input("Reply from server: ")
    
    #Send the server message to the client
    connection.send(response.encode("UTF-8")) 
    

#Close the TCP server
connection.close()
    
   