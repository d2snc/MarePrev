import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime


heights = []
t = []
freq = []
i=0

f = open('dadosfortal.txt', 'r')
for i, line in enumerate(f):
    if int(line.split()[4]) > 0:
        t.append(datetime.strptime(" ".join(line.split()[:4]), "%Y %m %d %H"))
        heights.append(0.001*float(line.split()[4]))
    i +=1
    freq.append(i)
f.close()


plt.figure(figsize=(100,30))
plt.figure(1)
plt.subplot(211)
plt.plot(t, heights, label="Observado")
plt.title('Nível do Mar - Fortaleza - 2008-2020 - Tempo')
plt.xlabel('Mês-Dia-Horas')
plt.ylabel('Metros')

plt.subplot(212)
plt.hist(heights,bins=25)
plt.title('Nível do Mar - Fortaleza - 2008-2020 - Frequência')
plt.xlabel('Altura(m)')
plt.ylabel('Ocorrências')

plt.show()
