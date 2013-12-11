
str = raw_input('test')
if str.isdigit():
	num = int(str)	
	print num
	tmp  = num + 10
	print tmp
	print num + tmp
else :
	while str:
		print str
		str = str[1:]

