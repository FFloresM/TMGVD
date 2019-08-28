#pasar a string
#para proyecto revisar clustering lsh
#programar countcy y count-sketch
import random as rd
import numpy as np

class Count_min():
	hashes = {}
	"""docstring for hash"""
	def __init__(self, d):
		p = (2<<31)-1
		delta = rd.random()
		self.d = d

	def hash(self, a, b, p):
		for i in self.d:
			a = rd.randint(p)
			b = rd.randint(p)
			self.hashes.append( 
				lambda x,w : ((a*x+b)%p)%w
				)




class sketch():
	"""docstring for sketch"""
	
	def __init__(self, delta, eps):
		d = int(np.log2(1/delta)) 
		w = int(4/eps)	
		self.matriz = np.zeros((d,w), dtype=int)

	def update(self, x, hashes):
		for i in range(len(hashes)):
			self.matriz[i, hashes[i](x)] += 1

	def query(self, x):
		values = []
		for i in range(len(hashes)):
			values.append(self.matriz[i,hashes[i](x)]) 
		return min(values)
			

		


