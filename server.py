# COEN498 PP: Cloud Computing
# Javier E. Fajardo - 26487602

# server.py: core logic for the server handling requests

import os
import sys
import socket

import socketserver

from common import *
from animals import *

# TODO: put the honeybadger here
AnimalSecret = Honeybadger

class AssignmentRequestHandler(socketserver.BaseRequestHandler):
	"""
	The RequestHandler class for our server.

	It is instantiated once per connection to the server, deals with the request as needed
	"""
	
	def challenge(self):
		pass
	

	def handle(self):
		def handleJSONClient(json_data):
			pass
	
		def handleProtobufClient(proto_data):
			pass
			
		while True:
			
			# self.request is the TCP socket connected to the client
			self.data = self.request.recv(4096).strip()
			if(self.data.decode()=="close" or len(self.data)<1):
				break
			print("{} wrote:".format(self.client_address[0]))
			print(self.data)
			# just send back the same data, but upper-cased
			self.request.sendall(self.data.upper())
#end AssignmentRequestHandler

def say():
	pass

def main(args):
	# We have to make sure the remote server binds to all interfaces, not just localhost
	HOST= "0.0.0.0"

	# Create the server, binding to localhost on port 9999
	server = socketserver.TCPServer((HOST, PORT), AssignmentRequestHandler)

	# Activate the server; this will keep running until you
	# interrupt the program with Ctrl-C
	server.serve_forever()
#end main

if __name__=="__main__":
	main(sys.argv[1:])