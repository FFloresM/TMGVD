
import numpy as np
import hashlib

class LogLog:
	"""docstring for LogLog"""
	def __init__(self, arg=None):
		self.arg = arg
		
	def index_least1(self,x):
		if x ==0:
			return 0
		index = 1
		while x%2==0:
			x>>=1 
			index+=1
		return index

	def least1(self, x, L):
		if x == 0:
			return 2**L
		return x & -x

	def cardinalidad(self, buckets):
		buckets = [self.index_least1(x) for x in buckets]
		return 0.77351 * len(buckets) * 2 ** (np.mean(buckets))

	def hash(self, s):
		return int(hashlib.sha1(s).hexdigest(), 16) & 0xffffff