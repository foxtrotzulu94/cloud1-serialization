import os
import sys
import socket

from common import *

def say():
	pass
	
def textSerializationClient():
	pass

def profobufSerializationClient():
	pass
	
def main(args):
	HOST = "localhost" # for now
	link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	link.connect((HOST,PORT))
	link.send('close'.encode())
	print(link.recv(4096))
	link.close()
#end main

if __name__=="__main__":
	main(sys.argv[1:])