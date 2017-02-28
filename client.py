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
		
	def isLeaf(self):
		return self.right is None and self.left is None
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
		
	def evaluateResponse(self,isTrue):
		if isTrue:
			self.moveRight()
		else:
			self.moveLeft()
#end qtree

def MakeQuestionTree():
	# build all of the questions that the client will ask to guess the animal
	root_question = Node(Question('qualities','mammal'), Node(Question('quality','large')), Node(Question('colors','black')))
	root_question.left.left = Node(Question('name','Gecko'))
	root_question.left.right = Node(Question('name','KomodoDragon'))
	
	follow_up = Node(Question('qualities','carnivore'),Node(Question('name','Sheep')),Node(Question('features','fur')))
	root_question.right.left = follow_up
	root_question.right.right = follow_up
	
	follow_up.right.left = Node(Question('qualities','aquatic'),None,Node(Question('name','Orca')))
	follow_up.right.right = Node(Question('qualities','domesticated'),Node(Question('name','Honeybadger')),Node(Question('name','Dog')))
	
	return QuestionTree(root_question)
#end MakeQuestionTree

def serverSays(something, *args):
	if args is not None:
		print("SERVER: "+something.format(*args))
	else:
		print("SERVER: "+something)
	
def clientSays(something, *args):
	if args is not None:
		print("CLIENT: "+something.format(*args))
	else:
		print("CLIENT: "+something)
	
def jsonClient(socket_link, qtree):
	socket_link.send('json'.encode())
	serverSays(socket_link.recv(4096).decode())
	# now just play the game!
	#while qtree.root is not None:
	current_question = qtree.root.value
	clientSays(str(current_question))
	socket_link.send(current_question.serializeJSON().encode())
	current_answer = Answer()
	raw_answer = socket_link.recv(4096).decode()
	current_answer.deserializeJSON(raw_answer)
	serverSays('{}',current_answer.readable())

def profobufClient(socket_link, qtree):
	# TODO!!!
	raise NotImplementedError
	
def main(args):
	print(args)
	handlers = {'json':jsonClient, 'protobuf': profobufClient}
	
	# Validate the serialization mode
	if args[1] in handlers:
		qtree = MakeQuestionTree()
		host = args[0]
		port = PORT
		
		clientSays("Connecting to server ...")
		link = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		link.connect((host,port))
		# do the whole handshake thing
		link.send(CLIENT_ID.encode())
		serverSays(link.recv(4096).strip().decode())
		link.send(CHALLENGE.encode())
		serverSays(link.recv(4096).strip().decode())
		
		# if the connection is still alive, hand it off to a specialized function
		handlers[args[1]](link,qtree)
		
		link.close()
		# except Exception as e:
			# print(e)
			# print("Client failed. Aborting")
			# exit(1)
	else:
		print("Serialization mode '{}' not recognized only {} are valid".format(args[1],str(handlers.keys)))
		exit(1)	
#end main

if __name__=="__main__":
	args = sys.argv[1:]
	if len(args) <2:
		if not DEFAULTS:
			print("COEN498 Assignment 1 Client")
			print("Usage: python3 client.py <Server IP> <Serialization Mode (json or protobuf)>")
			exit(1)
		else:
			print("Using defaults arguments")
			args = DEF_ARGS
	main(args)