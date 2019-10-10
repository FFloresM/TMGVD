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
delta = 0.001
eps = 0.002
data = dg.zipf(a=1.5,n=10000000)
skt = sys.argv[1]
if skt not in alg.keys():
	exit("Ingrese entrada válida")
print(alg[skt])
used_sketch = None

if skt=='cm':
	cm = CountMin(delta, eps)
	ti_skt = time.time()
	for i in data:
		cm.update(i)
	te_skt = time.time()
	used_sketch = cm

elif skt == 'cs':
	cs = CountSketch(delta,eps)
	ti_skt = time.time()
	for i in data:
		cs.update(i)
	te_skt = time.time()
	used_sketch = cs

elif skt=='cmcu':
	cmcu = CountMinCU(delta,eps)
	ti_skt = time.time()
	for i in data:
		cmcu.update(i)
	te_skt = time.time()
	used_sketch = cmcu


##HH test
phi = 0.1
ti_f_real = time.time()
hh = HeavyHitter(used_sketch, data)
te_f_real = time.time()
#heavy hitters reales
t_ir = time.time()
print(hh.HH_real(phi))
t_er = time.time()
#heavy hitters estimados según sketch
t_ie = time.time()
print(hh.HH_est(phi))
t_ee = time.time()

print("t_f_real", te_f_real - ti_f_real, 'seg.')
print("t_skt_build", te_skt-ti_skt, 'seg.')
print("t_hh_real ", (t_er - t_ir), 'seg.')
print("t_hh_estimado ", (t_ee - t_ie), 'seg.')
print("mem ",sys.getsizeof(used_sketch.sketch))
print(sys.getsizeof(hh.f_real))


