# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:57 2018

@author: Arlo Eardley 1108472
"""
import socket

# Establish a TCP connection - no arguments in sockt() is by dfault TCP

TCPsocket =socket.socket()

# Bind teh socket to the 127.0.0.1  IP local host and port has been selected as 7000
TCPsocket.bind(('127.0.0.1', 7000)) 

# Listens for connections with number of backoog connections set to 5
TCPsocket.listen(5)

# Accept connections from client at same port of 7000
connection, address = TCPsocket.accept() 


print ("Connection request from address: " + str(address))

#Receive the message from the client
ReceivedFromClient = connection.recv(4096).decode("UTF-8")

#Print out the message received 
print(ReceivedFromClient) 

#Close the connection
connection.close()
    
   