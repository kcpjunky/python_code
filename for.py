D = {'a':1,'b':2,'c':3}

print(D)

Ks = D.keys()

Ks.sort()
print(Ks)

for key in sorted(D) :
	print key, '=>', D[key]

for key in sorted(D) :
	D[key] = D[key] + 1
	print key, '=>', D[key]


for c in 'spam' :
	print c.upper()

print D.has_key('f')


T =  (1,2,3,4)
len(T)

T + (5,'name')
print (T)