def maker(n):
	def action(x):
		return x ** n
return action

f = maker(2)
t = maker(4)
f(2)
t(3)
