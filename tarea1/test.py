from sketchs import CountMin, CountSketch, CountMinCU, HeavyHitter
import data_gen as dg
import random as rd

delta = 0.01
eps = 0.02
cm = CountMin(delta, eps)
#print("d=", cm.d, "w=", cm.w)

#data = dg.randomString(100000)
data = dg.zipf(n=100000)
v = '1'

for i in data:
	cm.update(i)

print(cm.query(v))

cs = CountSketch(delta,eps)
#print("d=", cs.d, "w=", cs.w)
for i in data:
	cs.update(i)
print(cs.query(v))

cmcu = CountMinCU(delta,eps)
#print("d=", cmcu.d, "w=", cmcu.w)
for i in data:
	cmcu.update(i)
print(cmcu.query(v))

##HH test
hh = HeavyHitter(cs.sketch, data)
print(hh.f_real)