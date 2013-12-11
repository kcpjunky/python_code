text = 'hello world'
print ord(text[1])

print 'for'

for ch in text:
	print ord(ch)


listText = list(text)

print listText

encText =[]
for ys in listText:
	encText.append(ord(ys))

print encText


print map(ord, text)
