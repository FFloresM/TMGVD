import random
import string
import numpy as np

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def zipf(a=2,n=100):
	"""generate random numbers with zipf distribution"""
	x = np.random.zipf(a,n)
	x = [str(i) for i in x]
	return x

def kmers(k=5,n=1, path_to_file=""):
	kmers = []
	conj = {}
	with open(path_to_file, 'r') as file:
		lines = [next(file) for x in range(n)]
	
	for line in lines:
		for s in range(len(line)):
			kmer = line[s:k+s]
			if len(kmer) == k :
				if kmer.isalpha():
					kmers.append(kmer)

	return kmers


		

		