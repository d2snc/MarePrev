import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


heights = []
t = []
freq = []
i=0

f = open('dadosmadeira.txt', 'r')
for i, line in enumerate(f):
    if int(line.split()[2]) > 0:
        t.append(datetime.strptime(" ".join(line.split()[:2]), "%d/%m/%Y %H:%M:%S"))
        heights.append(0.01 * float(line.split()[2]))
        i +=1
        freq.append(i)
f.close()

plt.figure(figsize=(100,30))
plt.figure(1)
plt.subplot(211)
plt.plot(t, heights, label="Observado")
plt.title('Nível do Mar - Madeira - 1991-2013 - Tempo')
plt.xlabel('Mês-Dia-Horas')
plt.ylabel('Metros')

plt.subplot(212)
plt.hist(heights,bins=25)
plt.title('Nível do Mar - Madeira - 1991-2013 - Frequência')
plt.xlabel('Altura(m)')
plt.ylabel('Ocorrências')

plt.show()


