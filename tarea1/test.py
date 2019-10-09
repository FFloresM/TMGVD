"""
Test para datos sintéticos de CountMin, CountMinSketch y CountMinCU
Estimación de Heavy-Hitters con datos sintéticos de zipf
cm: CountMin, 
cs: CountSketch, 
cmcu: CountMinCU

"""

from sketchs import CountMin, CountSketch, CountMinCU, HeavyHitter
import data_gen as dg
import random as rd
import time
import sys

alg = {
	'cm': 'CountMin', 
	'cs': 'CountSketch', 
	'cmcu': 'CountMinCU',
	}
delta = 0.01
eps = 0.02
data = dg.zipf(n=10000000)
skt = sys.argv[1]
if skt not in alg.keys():
	exit("Ingrese entrada válida")
print(alg[skt])
used_sketch = None

if skt=='cm':
	cm = CountMin(delta, eps)
	for i in data:
		cm.update(i)
	used_sketch = cm

elif skt == 'cs':
	cs = CountSketch(delta,eps)
	for i in data:
		cs.update(i)
	used_sketch = cs

elif skt=='cmcu':
	cmcu = CountMinCU(delta,eps)
	for i in data:
		cmcu.update(i)
	used_sketch = cmcu


##HH test
phi = 0.1
hh = HeavyHitter(used_sketch, data)

t_ir = time.time()
print(hh.HH_real(phi))
t_er = time.time()

t_ie = time.time()
print(hh.HH_est(phi))
t_ee = time.time()

print("real ", (t_er - t_ir), 'seg.')
print("estimado ", (t_ee - t_ie), 'seg.')
print("mem ",sys.getsizeof(used_sketch.sketch))
print(sys.getsizeof(hh.f_real))


