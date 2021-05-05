import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pytides.tide import Tide

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

#For a quicker decomposition, we'll only use hourly readings rather than 6-minutely readings.
#heights = np.array(heights[::10])
#t = np.array(t[::10])

##Prepare a list of datetimes, each 6 minutes apart, for a week.
prediction_t0 = datetime(2013,1,1) #mudei aq
hours = 0.1*np.arange(7 * 24 * 10)
times = Tide._times(prediction_t0, hours)

##Fit the tidal data to the harmonic model using Pytides
my_tide = Tide.decompose(heights, t)
##Predict the tides using the Pytides model.
my_prediction = my_tide.at(times)

print(hours)
exit()

plt.figure(figsize=(100,30))
plt.figure(1)
plt.subplot(311)
plt.plot(t, heights, label="Observado")
plt.title('Nível do Mar - Belém - 1963-1967 - Tempo')
plt.xlabel('Mês-Dia-Horas')
plt.ylabel('Metros')

plt.plot(hours, my_prediction,color='black', label="Predição Pytides") #Previsão de maré criada pelo Pytides
plt.legend()
plt.title('Previsão criada por Pytides: ')
plt.xlabel('Horas desde ')
plt.ylabel('Metros')



plt.subplot(312)
plt.hist(heights,bins=25)
plt.title('Nível do Mar - Belém - 1963-1967 - Frequência')
plt.xlabel('Altura(m)')
plt.ylabel('Ocorrências')



plt.show()





