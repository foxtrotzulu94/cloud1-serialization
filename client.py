# COEN498 PP: Cloud Computing
# Javier E. Fajardo - 26487602

# client.py: core logic for all client functionality

import os
import sys
import socket
from time import sleep

from common import *

### Client globals
# Run the script using the defualt operation mode
DEFAULTS = False
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
		self.root = self.root.left
		return self.root

	def moveRight(self):
		self.root = self.root.right
		return self.root
		
	def evaluateResponse(self,isTrue):
		if isTrue:
			self.moveRight()
		else:
			self.moveLeft()
#end qtree

def MakeQuestionTree():
	# build all of the questions that the client will ask to guess the animal
	root_question = Node(Question('qualities','mammal'), Node(Question('qualities','large')), Node(Question('colors','black')))
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
#end serverSays
	
def clientSays(something, *args):
	if args is not None:
		print("CLIENT: "+something.format(*args))
	else:
		print("CLIENT: "+something)
#end clientSays
	
def PlayTheGame(socket_link, mode, qtree):
	socket_link.send(mode.encode())
	serverSays(socket_link.recv(4096).decode())
	print()
	clientSays("Let's play the guessing animal game!")
	# now just play the game!
	current_answer = Answer()
	while qtree.root is not None:
		sleep(0.5) # Delay showing the question on the screen
		current_question = qtree.root.value
		clientSays(str(current_question))
		socket_link.send(current_question.serialize(mode))
		current_answer = Answer()
		raw_answer = socket_link.recv(4096)
		current_answer.deserialize(mode,raw_answer)
		
		sleep(0.5)  # Delay showing the answer
		serverSays('{}',current_answer.readable())
		
		if current_answer.game_over:
			sleep(0.5)
			guessedAnimal = Animal()
			raw_animal = socket_link.recv(4096)
			guessedAnimal.deserialize(mode,raw_animal)
			clientSays("Guessed the right animal! It's a {}", guessedAnimal.name)
			print(str(guessedAnimal))
			# server closes connection automatically
			break
		
		if current_answer.response is True:
			qtree.moveRight()
		else:
			qtree.moveLeft()
#end PlayTheGame
	
def main(args):
	handlers = {'json', 'protobuf'}
	
	# Validate the serialization mode
	if args[1] in handlers:
		qtree = MakeQuestionTree()
		host = args[0]
		mode = args[1]
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
		PlayTheGame(link,mode,qtree)
		
		try:
			link.close()
		except Exception as e:
			clientSays("Closing")

	else:
		print("Serialization mode '{}' not recognized only {} are valid".format(args[1],str(handlers)))
		sys.exit(1)	
#end main

if __name__=="__main__":
	args = sys.argv[1:]
	print("COEN498 Assignment 1 Client")
	if len(args) <2:
		if not DEFAULTS:
			print("Usage: python3 client.py <Server IP> <Serialization Mode (json or protobuf)>")
			sys.exit(1)
		else:
			print("Using defaults arguments")
			args = DEF_ARGS
	main(args)