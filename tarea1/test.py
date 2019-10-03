from sketchs import CountMin
import random as rd

delta = 0.01
eps = 0.02
cm = CountMin(delta, eps)
print("d=", cm.d, "w=", cm.w)
#print(cm.hashes)
n = 10000000
data = [rd.randint(0,100000) for x in range(n)]

for i in data:
	cm.update(i)

print(cm.query(7))