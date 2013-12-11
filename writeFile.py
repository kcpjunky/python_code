#write text to new file
file = open('theFile.txt','w')
file.write('hello')

#file object should be closed after using
file.close()
