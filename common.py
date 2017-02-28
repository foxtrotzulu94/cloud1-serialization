# COEN498 PP: Cloud Computing
# Javier E. Fajardo - 26487602

# common.py: some data and definitions necessary for both client and server
from binascii import hexlify, unhexlify
from hashlib import md5

# common port to use
PORT = 4981

# hex string used for challenge. We don't want to get hung up in other connections
CHALLENGE = hexlify(md5('h'.encode()).digest()).decode()

class serializable():
	"""
	Interface class for serialization in this assignment.
	Not common in Python, but makes sure that we have both the protobuf and the json
	"""
	def serializeJSON():
		raise NotImplementedError
	
	def serializeProto():
		raise NotImplementedError
#end class serializable

class Animal(serializable):
	def __init__():
		pass
	#end 
	
	# TODO: override serializeJSON and serializeProto
#end class animal

class Honeybadger(Animal):
	pass
#end

class Question(serializable):
	def __init__():
		pass
	#end 
	# TODO: override serializeJSON and serializeProto
#end class

class Answer(serializable):
	def __init__():
		pass
	#end 
	# TODO: override serializeJSON and serializeProto
#end class