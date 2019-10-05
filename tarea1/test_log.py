from log import LogLog
import pandas as pd
import numpy as np

words = ['h', 'm', 'h', 'm', 'p', 'a','h', 'm', 'h', 'm', 'p', 'a','r','b','c']	
words = [x.lower().encode('utf-8') for x in words]

df = pd.DataFrame(data=np.nan, index=range(0, 3 * len(words)), columns=['f', 'x', 'count'])

ll = LogLog()

s = set()
bitmap = 0
buckets16 = np.array([0]*16)
buckets64 = np.array([0]*64)

for idx, w in enumerate(words):
	s.add(w)
	hashed = ll.hash(w)

	bitmap |= ll.least1(hashed, 24)

	buckets16[hashed % 16] = max(buckets16[hashed % 16], ll.least1(hashed >> 4, 24))
	buckets64[hashed % 64] = max(buckets64[hashed % 64], ll.least1(hashed >> 6, 24))

	df.loc[idx * 4] = ['True Counting', idx, len(s)]
	df.loc[idx * 4 + 1] = ['LogLog (16 buckets)', idx, ll.cardinalidad(buckets16)]
	df.loc[idx * 4 + 2] = ['LogLog (64 buckets)', idx, ll.cardinalidad(buckets64)]

print(df)