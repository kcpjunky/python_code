str1 = raw_input('please input')

if not str1:
	print 'you are failed'

while str1:
	print str1,
	str1 = str1[1:]
