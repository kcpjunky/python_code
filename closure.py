def func1():
	x = 100
	def func2():
		print x
	return func2

action = func1()
action()
