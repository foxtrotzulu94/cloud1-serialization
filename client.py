# COEN498 PP: Cloud Computing
# Javier E. Fajardo - 26487602

# client.py: core logic for all client functionality

import os
import sys
import socket

from common import *

### Client globals
# Run the script using the defualt operation mode
DEFAULTS = True
HOST = "localhost"
SERIALIZATION = "json"
DEF_ARGS = [HOST,SERIALIZATION]
### end client globals

class Node():
	def __init__(self,value=None,left=None,right=None):
		self.value = value
		self.left = left
		self.right = right
# end class node

class QuestionTree():
	def __init__(self, root):
		self.root = root
		
	def moveLeft(self):
		self.root = root.left
		return self.root

	def moveRight(self):
		self.root = root.right
		return self.root
#end qtree

def MakeQuestionTree():
	pass
	
def jsonClient(socket_link):
	socket_link.send('json'.encode())
	socket_link.recv(4096)

def profobufClient(socket_link):
	pass
	
def main(args):
	print(args)
	handlers = {'json':jsonClient, 'proto': profobufClient}
	
	# Validate the serialization mode
	if args[1] in handlers:
		MakeQuestionTree()
		host = args[0]
		port = PORT
		try:
			link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			link.connect((host,port))
			
			handlers[args[1]](link)
			link.close()
		except Exception as e:
			print(e)
			print("Client failed. Aborting")
	else:
		print("Serialization mode '{}' not recognized only {} are valid".format(args[1],str(handlers.keys)))
		exit(1)	
#end main

if __name__=="__main__":
	args = sys.argv[1:]
	if len(args) <2:
		if not DEFAULTS:
			print("COEN498 Assignment 1 Client")
			print("Usage: python3 client.py <Server IP> <Serialization Mode (json or proto)>")
			exit(1)
		else:
			print("Using defaults arguments")
			args = DEF_ARGS
	main(args)