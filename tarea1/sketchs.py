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
		print('d = ', self.d, 'W = ', self.w)
		
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
		print('d = ', self.d, 'W = ', self.w)

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
		
		
class HeavyHitter():
	"""docstring for HeavyHitter"""
	def __init__(self, count, stream):
		self.count = count
		self.sketch = self.count.sketch
		self.set, self.f_real = self.frecuency(stream)
		self.total_len = len(stream)

		#test
		print('n =',self.total_len, "SET :",len(self.set))

	def frecuency(self, stream):
		conj = set()
		for i in stream:
			conj.add(i)
		dic = {v:0 for v in conj}
		for i in stream:
			dic[i]+=1

		return conj, dic

	def HH_real(self, value):
		"""values es % respecto del total de elementos"""
		#freal = sort(self.freal)
		hh ={}
		per = self.total_len*value
		for x in self.f_real:
			if self.f_real[x] >= per:
				hh[x] = self.f_real[x]

		return hh

	def HH_est(self, value):
		""" hh estimado"""
		hh_est ={} ##heavy-hitters estimado
		f_est = {} #frecuencias estimadas desde sketchs
		total_len_est = 0 #cantidad total en el strem segun sketch
		
		for x in self.set:
			v = self.count.query(x)
			f_est[x] = v
			total_len_est += v	

		per = total_len_est*value
		for j in f_est:
			if f_est[j] >= per:
				hh_est[j] = f_est[j]

		print("total len est :",total_len_est)
		return hh_est
		