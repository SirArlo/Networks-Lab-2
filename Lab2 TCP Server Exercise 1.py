# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:57 2018

@author: eards
"""
import socket

TCPsocket =socket.socket()
TCPsocket.bind(('127.0.0.1', 7000)) # The 127.0.0.1  IP is for local host and port has been selected as 7000
TCPsocket.listen(5)  # Listens for connection with number of backoog connections set to 5
connection, address = TCPsocket.accept() 
# binds the socket to adress and listens for connections with the arguments of connection and adress bound to socket

#print ("Connected to socket address"+ address + "and IP "
print ("Connection request from address: " + str(address))
ReceivedFromClient = connection.recv(4096).decode("UTF-8")
print(ReceivedFromClient) 
connection.close()
    
   