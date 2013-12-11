while True:
	reply = raw_input('enter text')
	if reply == 'stop':
		break
	elif not reply.isdigit():
		print 'bat'*8
	else:
		num = int(reply)
		if num < 20:
			print 'low'
		else:
			print num ** 2
print 'bye'
