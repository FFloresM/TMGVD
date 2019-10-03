import random as rd

def hash(p=(2<<32)-1):
	hashes = []
	for i in range(4):
		a = rd.randint(1,p)
		b = rd.randint(1,p)
		hashes.append(lambda x: ((a*x+b)%p)%50 )
	return hashes

hashes = hash()

print(hashes[0](1))
print(hashes[1](1))


