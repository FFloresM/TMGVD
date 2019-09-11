"""Similitud en documentos
	usando minhash
"""
import random as rd

doc1 = "holamundo"
doc2 = "bolaturdo"

def k_shingles(doc, k):
	# retorna una lista de k-shingles
	sg = []
	for i in range(len(doc)):
		s = doc[i:k+i]
		if len(s) == k:
			sg.append(s)
	return sg



class minHash():
	"""docstring for minHash"""
	
	hashes = []
	a_b = [] 
	def __init__(self, N, p=10007):
		self.n = N
		self.p = p
		for i in range(N):
			a = rd.randint(1,p)
			b = rd.randint(1,p)
			self.a_b.append((a,b))

	def hash(self, a, b):
		return lambda x : (a*x+b)%self.p

	def setHashes(self):
		for i in self.a_b:
			h = self.hash(i[0],i[1])
			self.hashes.append(h)

	def getHashes(self):
		return self.hashes

	def getAB(self):
		return self.a_b


if __name__ == '__main__':

	shingle_doc1 = k_shingles(doc1,3)
	shingle_doc2 = k_shingles(doc2,3)

	h_doc1 = []
	h_doc2 = []

	for i in shingle_doc1:
		h_doc1.append(hash(i))

	for i in shingle_doc2:
		h_doc2.append(hash(i))

	hsh = minHash(8)
	hsh.setHashes()
	print(hsh.getHashes())

	##continuar probando cada hash en todo el h_doc1 y h_doc2



	#print(shingle_doc1)
	#print(h_doc1)




	