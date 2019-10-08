"""
Test para datos sintéticos de CountMin, CountMinSketch y CountMinCU
Estimación de Heavy-Hitters con datos sintéticos de zipf

"""

from sketchs import CountMin, CountSketch, CountMinCU, HeavyHitter
import data_gen as dg
import random as rd

delta = 0.01
eps = 0.02
cm = CountMin(delta, eps)
#print("d=", cm.d, "w=", cm.w)

#data = dg.randomString(1000)
data = dg.zipf(n=1000000)

for i in data:
	cm.update(i)

#print(cm.query(v))

cs = CountSketch(delta,eps)
#print("d=", cs.d, "w=", cs.w)
for i in data:
	cs.update(i)
#print(cs.query(v))

cmcu = CountMinCU(delta,eps)
#print("d=", cmcu.d, "w=", cmcu.w)
for i in data:
	cmcu.update(i)
#print(cmcu.query(v))

##HH test
phi = 0.1
hh = HeavyHitter(cm, data)
print(hh.HH_real(phi))
print(hh.HH_est(phi))

hh = HeavyHitter(cs, data)
print(hh.HH_est(phi))

hh = HeavyHitter(cmcu, data)
print(hh.HH_est(phi))
