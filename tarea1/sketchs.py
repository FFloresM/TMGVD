import random as rd
import numpy as np
import math as mt
import mmh3

class CountMin:
	"""docstring for CountMin"""
	def __init__(self, delta, epsilon):
		self.d = int(mt.log(1/delta))
		self.w = int(mt.exp(1)/epsilon)
		self.sketch = np.zeros((self.d,self.w), dtype=int)
		
	def index(self, x, i):
		"""value x, seed i"""
		return mmh3.hash(x,i,signed=False)%self.w

	def update(self, x):
		for i in range(self.d):
			self.sketch[i, self.index(x,i)] +=1


	def query(self, x):
		values = []
		for i in range(self.d):
			values.append(self.sketch[i, self.index(x,i)])
		return min(values)


class CountSketch():
	"""docstring for CountSketch"""
	def __init__(self, delta, epsilon):
		self.d = int(mt.log(4/delta))
		self.w = int(1/(epsilon**2))
		self.sketch = np.zeros((self.d,self.w), dtype=int)

	def index(self, x, i):
		"""value x, seed i"""
		return mmh3.hash(x,i,signed=False)%self.w

	def g(self, x, i):
		return 1 if mmh3.hash(x,i) > 0 else -1

	def update(self, x):
		for i in range(self.d):
			self.sketch[i, self.index(x,i)] += self.g(x,i) 

	def query(self, x):
		values = []
		for i in range(self.d):
			values.append(self.sketch[i, self.index(x,i)]*self.g(x,i))
		return np.median(values)

class CountMinCU(CountMin):
	"""docstring for CountMinCU"""
	def __init__(self, delta, epsilon):
		CountMin.__init__(self, delta, epsilon)

	def update(self, x):
		minimos = []
		for i in range(self.d):
			for j in range(self.d):
				minimos.append(self.sketch[i, self.index(x,i)])
			_min = min(minimos)
			if self.sketch[i, self.index(x,i)] == _min:
				self.sketch[i, self.index(x,i)] +=1

	def query(self, x):
		return super().query(x)
		
		