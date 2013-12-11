f = open('test.txt', 'w')
f.write('hello\n')
f.write('text\n')

f.close()

f=open('test.txt')
bytes = f.read()
bytes