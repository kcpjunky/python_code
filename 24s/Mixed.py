class MixedNames:
	#class object property
	data = 'spam'

	#init 
	def __init__(self, value):
		self.data = value
	
	def display(self):
		print self.data, MixedNames.data
