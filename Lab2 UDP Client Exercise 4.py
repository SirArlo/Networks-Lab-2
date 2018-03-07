# -*- coding: utf-8 -*-
#!/usr/bin/python 
"""
Created on Thu Feb 22 17:02:08 2018

@author: Arlo Eardley 1108472
"""

import socket
serverPort = 7000

#establish a UDP client
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Allow the Client to send data to server
message = raw_input("Message to server:")

#While teh client is still connected
while message != 'q':
    
    #Send the message to the server
    clientSocket.sendto(message,("127.0.0.1", serverPort))
    
    #Receive message back from the server
    ReceivedFromServer, serverAddress = clientSocket.recvfrom(2048)
    
    #Print out the server reply 
    print("Server Reply:" + str(ReceivedFromServer))
    
    #Allow the client to send a new message
    message = raw_input("Message to server:")


#Send last message to server to let it know the client has disconnected
clientSocket.sendto(message,("127.0.0.1", serverPort))

#Close the UDP connection
clientSocket.close()


