# COEN498 PP: Cloud Computing
# Javier E. Fajardo - 26487602

# common.py: some data and definitions necessary for both client and server
import json
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
	def serializeJSON(self):
		"""Makes a valid json string of 'most' objects. Subclasses may not be easily transformed into dicts"""
		return json.dumps(self.__dict__)
	
	def serializeProto(self):
		raise NotImplementedError
		
	def deserializeJSON(self, json_data):
		raise NotImplementedError
	
	def deserializeProto(self, proto_data):
		raise NotImplementedError
#end class serializable

class Animal(serializable):
	"""Common animal class"""

	def __init__(self):
		"""Constructor"""
		self.name = type(self).__name__
		self.qualities = []
		self.abilities = []
		self.features = []
		self.colors = []
	#end 

	def serializeProto(self):
		raise NotImplementedError
		
	def deserializeJSON(self, json_data):
		self_obj = json.loads(json_data)
		self.name = self_obj['name']
		self.abilities = self_obj['abilities']
		self.qualities = self_obj['qualities']
		self.features = self_obj['features']
		self.colors = self_obj['colors']
	
	def deserializeProto(self, proto_data):
		raise NotImplementedError
	
#end class animal

class Question(serializable):
	"""Class for wrapping the question being sent between client and server"""
	def __init__(self, q_type=None, q_guess=None):
		self.inquiry = q_type
		self.guess = q_guess
	#end 
	
	# TODO: override serializeProto
	def serializeProto(self):
		raise NotImplementedError
		
	def deserializeJSON(self, json_data):
		self_obj = json.loads(json_data)
		self.inquiry = self_obj['inquiry']
		self.guess = self_obj['guess']
	
	def deserializeProto(self, proto_data):
		raise NotImplementedError
#end class

class Answer(serializable):
	"""Class for wrapping the answer being sent between client and server"""
	def __init__(self, question=None, value=None):
		self.question = question
		self.response = value
	#end 
	
	# TODO: override and serializeProto
	def serializeJSON(self):
		"""Makes a valid json string of this object"""
		question_dict = self.question.__dict__
		this_dict = self.__dict__
		this_dict['question'] = question_dict
		return json.dumps(this_dict)
	
	def serializeProto(self):
		raise NotImplementedError
		
	def deserializeJSON(self, json_data):
		self_obj = json.loads(json_data)		
		self.response = self_obj['response']
		self.question.deserializeJSON(self_obj['question'])
	
	def deserializeProto(self, proto_data):
		raise NotImplementedError
#end class