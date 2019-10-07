from log import LogLog
import data_gen as dg
import pandas as pd
import numpy as np

words = dg.randomString(6000)	
words = [x.lower().encode('utf-8') for x in words]

ll = LogLog()

s = set()
bitmap = 0
buckets16 = np.array([0]*16)
buckets64 = np.array([0]*64)
result = []

for idx, w in enumerate(words):
	s.add(w)
	hashed = ll.hash(w)

	bitmap |= ll.least1(hashed, 24)

	buckets16[hashed % 16] = max(buckets16[hashed % 16], ll.least1(hashed >> 4, 24))
	buckets64[hashed % 64] = max(buckets64[hashed % 64], ll.least1(hashed >> 6, 24))

	result.append([len(s), ll.cardinalidad(buckets16), ll.cardinalidad(buckets64)])

for i in range(len(result)):
	print(i+1, result[i])