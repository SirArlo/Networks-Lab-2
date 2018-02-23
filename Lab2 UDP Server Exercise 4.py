# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:08 2018

@author: eards
"""

import socket
serverPort = 7000

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serverSocket.bind(("127.0.0.1", serverPort))
print("The server is ready to receive")
while 1:

    MessageFromClient, clientAddress = serverSocket.recvfrom(2048)
    
    if MessageFromClient == 'q':
        print("Connection terminated by client")
        break;
        
    print("Message from client:" + str(MessageFromClient))
    ReplyFromServer = raw_input("Server Reply: ")
    serverSocket.sendto(ReplyFromServer, clientAddress)

serverSocket.close()



