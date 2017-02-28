# COEN498 PP: Cloud Computing
# Javier E. Fajardo - 26487602

from common import Animal

class Honeybadger(Animal):
	def __init__(self):
		"""Constructor"""
		self.name = type(self).__name__
		self.qualities = ['carnivore','predator','mammal','small']
		self.abilities = ['walk','run','mate']
		self.features = list(Animals._features)
		self.colors = ['black','grey','white']
	#end 
#end

class Dog(Animal):
	def __init__(self):
		"""Constructor"""
		self.name = type(self).__name__
		self.qualities = ['omnivore','predator','mammal','carnivore']
		self.abilities = ['walk','run','mate']
		self.features = list(Animals._features)
		self.colors = ['black','grey','white']
	#end 
#end 

class Sheep(Animal):
	def __init__(self):
		"""Constructor"""
		self.name = type(self).__name__
		self.qualities = ['prey','herbivore']
		self.abilities = ['walk','run','mate']
		self.features = ['fur','tail','bones']
		self.colors = ['white','grey']
	#end 
#end

class Orca(Animal):
	def __init__(self):
		"""Constructor"""
		self.name = type(self).__name__
		self.qualities = ['carnivore','predator','mammal','large','aquatic']
		self.abilities = ['walk','run','mate','swim']
		self.features = ['teeth','tail','bones']
		self.colors = ['black','white']
	#end 
#end

class KomodoDragon(Animal):
	def __init__(self):
		"""Constructor"""
		self.name = type(self).__name__
		self.qualities = ['large','carnivore','predator','reptile']
		self.abilities = ['walk','run','lay eggs','swim']
		self.features = ['teeth','tail','scales']
		self.colors = ['green','grey']
	#end 
#end

class Gecko(Animal):
	def __init__(self):
		"""Constructor"""
		self.name = type(self).__name__
		self.qualities = ['small','carnivore','reptile']
		self.abilities = ['walk','lay eggs']
		self.features = ['tail']
		self.colors = ['grey','black','yellow','green']
	#end 
#end

KnownAnimals = [Honeybadger,Dog,Gecko,Orca,Sheep,KomodoDragon]
AnimalMap = {x.__name__:x for x in KnownAnimals}