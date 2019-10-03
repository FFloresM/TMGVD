import random as rd
import numpy as np
import math as mt

class CountMin:
	"""docstring for CountMin"""
	a = []
	b = []
	p = []
	def __init__(self, delta, epsilon):
		self.d = int(mt.log(1/delta))
		self.w = int(mt.exp(1)/epsilon)
		self.sketch = np.zeros((self.d,self.w), dtype=int)
		self.abp()

	def abp(self, p=(2<<32)-1):
		for i in range(self.d):
			P = rd.randint(1,p)
			a = rd.randint(1,P)
			b = rd.randint(1,P)
			self.a.append(a)
			self.b.append(b)
			self.p.append(P)

	def hash(self, x, i):
		return  ((self.a[i]*x+self.b[i])%self.p[i])%self.w

	def update(self, x):
		for i in range(self.d):
			self.sketch[i, self.hash(x,i)] +=1

	def query(self, x):
		values = []
		for i in range(self.d):
			values.append(self.sketch[i, self.hash(x,i)])
		return min(values)

