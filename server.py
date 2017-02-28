# COEN498 PP: Cloud Computing
# Javier E. Fajardo - 26487602

# server.py: core logic for the server handling requests

import os
import sys
import socket
import random
import datetime

import socketserver

from common import *
from animals import *

def log(something):
	timestamp = datetime.datetime.now
	print("{} SERVER: {}".format(timestamp(),something))
#end

class AssignmentRequestHandler(socketserver.BaseRequestHandler):
	"""
	The RequestHandler class for our server.

	It is instantiated once per connection to the server, deals with the request as needed
	"""	
	def handle(self):
		""" Write method here """
		supported_serializers = set(['json', 'protobuf'])
		
		# Initial connection
		remote_name = self.request.getpeername()
		log("Accepting connection from {}".format(remote_name))
		self.data = self.request.recv(4096).strip()
		msg = self.data.decode()
		
		#1. Client should identify themselves
		if msg!=CLIENT_ID:
			self.request.send("Wrong identification. Closing connection".encode())
			log("Client {} did not indentify itself".format(remote_name))
			return
		
		#2. Server send ok and waits for challenge
		self.request.send("Client ID OK from {}".format(SERVER_ID).encode())
		self.data = self.request.recv(4096).strip()
		msg = self.data.decode()
		if msg!=CHALLENGE:
			self.request.send("CHALLENGE FAILED".encode())
			log("Client failed to provide correct challenge")
			return
		log("Connected to client successfully")
		self.request.send("Challenge OK, serialization mode?".encode())
		
		# Check that the client is asking for a mode we expect
		self.data = self.request.recv(4096).strip()
		mode = self.data.decode()
		if mode not in supported_serializers:
			self.request.send("{} mode not found or not yet supported".format(mode).encode())
			log("Did not understand mode {} client was requesting".format(mode))
			return
		self.request.send("{} OK".format(mode).encode())
		
		log("Proceeding to animal game")
		# The secret animal that the client has to guess :)
		current_question = Question()
		#SecretAnimal = Honeybadger()
		SecretAnimal = random.choice(KnownAnimals)()
		secret_data = SecretAnimal.__dict__
		log("Client must guess {}".format(SecretAnimal.name))
		while True:
			# read the question
			question_data = self.request.recv(4096).strip()
			current_question.deserialize(mode,question_data)
			
			# answer the question and send it back over the wire
			current_answer = Answer(current_question, current_question.guess in secret_data[current_question.inquiry])
			if current_question.inquiry == 'name' and current_answer.response:
				log("Client guessed the name of the animal!")
				current_answer.game_over = True # The client guessed the name of our thing, good job!
				
			self.request.send(current_answer.serialize(mode))
			
			if current_answer.game_over:
				self.request.send(SecretAnimal.serialize(mode))
				log("Game with {} ended".format(remote_name))
				break
		# end while
#end AssignmentRequestHandler

def main(args):
	# We have to make sure the remote server binds to all interfaces, not just localhost
	HOST= "0.0.0.0"

	# Create the server, bind, and run until Ctrl+C is pressed
	server = socketserver.TCPServer((HOST, PORT), AssignmentRequestHandler)
	server.serve_forever()
#end main

if __name__=="__main__":
	print("Starting COEN498 Assignment 1 Server")
	print("Time {}".format(str(datetime.datetime.now())))
	main(sys.argv[1:])