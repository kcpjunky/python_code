while True:
	reply = raw_input('Enter text:')
	if reply == 'stop': break

	if reply.isdigit():
		print int(reply) * 2
print Bye
