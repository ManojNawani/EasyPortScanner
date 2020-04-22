#!/usr/bin/python

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#socket.AF_INET is for the IP_Address ipv4
#SOCK_STREAM is for TCP

host = raw_input("[*]Please Enter The Host To Scan:")
port = int(raw_input("[*]Please Enter The Port To Scan:"))

def portscanner(port):
    if mysock.connect_ex((host,port)):
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
