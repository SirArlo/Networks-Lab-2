# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:08 2018

@author: Arlo Eardley 1108472
"""

import socket
serverPort = 7000

#Establish a UDP server
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Bind to the ocal host
serverSocket.bind(("127.0.0.1", serverPort))


print("The server is ready to receive")

#While the client is still connected
while 1:
  
    #Receive the message from the client
    MessageFromClient, clientAddress = serverSocket.recvfrom(2048)
    
    #If the client is still connected
    if MessageFromClient <> 'q':
        
        #Print otu the message from the client
        print("Message from client:" + str(MessageFromClient))
        
        #Input a reply to teh client via user input
        ReplyFromServer = raw_input("Server Reply: ")
        
        #Send the reply to the client
        serverSocket.sendto(ReplyFromServer, clientAddress)





