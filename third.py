import subclass

class ThirdClass(subclass.subclass):
	def __init__(self, value):
		self.data = value
	def __add__(self, other):
		return ThirdClass(self.data + other)
	def __mul__(self, other):
		self.data = self.data * other


