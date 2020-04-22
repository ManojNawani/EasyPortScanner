#!/usr/bin/python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket.AF_INET is for the IP_Address ipv4
#SOCK_STREAM is for TCP

host = "10.1.1.1"
port = 443

def portscanner(port):
    if sock.connect_ex((host,port)):
        print "Port %d is Closed" % (port)
    else:
        print "Port %d is Open" % (port)

portscanner(port)


# We Define port scanner and if there is an error received
# then port id Closed.

#We can also use the f.string format to display port.
#print ('Port {} is Open'.format(port))


# To run the program
#./portscanner1.py
