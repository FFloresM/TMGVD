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

def prot(k=5,n=1000):
	f = open("/home/francisco/Descargas/proteinasunicas.fasta", 'r')
	data = f.read()
	subset = data[:n]
	for i in range(len(subset)):
		kmer = subset[i:n+1]
		print(kmer)

		