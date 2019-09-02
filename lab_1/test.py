import Countmin as cm
import random as rd
import numpy as np

data = np.random.randint(5,size=10)
print(data)

skt = cm.sketch(0.1,0.2)
print(skt.matriz)

