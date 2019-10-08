from sketchs import CountMin, CountSketch, CountMinCU, HeavyHitter
import data_gen as dg
import random as rd
import sys


path = sys.argv[1]
print(dg.kmers(k=5, n=1, path_to_file=path))