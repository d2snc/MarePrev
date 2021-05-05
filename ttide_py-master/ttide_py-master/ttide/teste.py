import ttide as tt
import numpy as np
import matplotlib.pyplot as plot
import math
from datetime import datetime


heights = []
t = []
freq = []
i=0

f = open('dadosbelem.txt', 'r')
for i, line in enumerate(f):
    if int(line.split()[2]) > 0:
        t.append(datetime.strptime(" ".join(line.split()[:2]), "%d/%m/%Y %H:%M"))
        heights.append(0.01 * float(line.split()[2]))
        i +=1
        freq.append(i)
f.close()

t = np.arange(1001) #t é um vetor que vai de 0 até 1000
m2_freq = 2 * np.pi / 12.42

elev = 5 * np.cos(m2_freq * t)

print(len(elev))
my_array = np.array(heights)
print(len(my_array))
tfit_e = tt.t_tide(elev,dt=1,lat=9)

