from datetime import datetime
from pytides.tide import Tide
import numpy as np
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta

def date_range(start_date, end_date, increment, period): #Função que usei para criar a lista de datetimes
    result = []
    nxt = start_date
    delta = relativedelta(**{period:increment})
    while nxt <= end_date:
        result.append(nxt)
        nxt += delta
    return result

#Com esse modelo eu adquiro os dados sobre as marés e consigo prever a maré para a data prevista

heights = []
t = []

f = open('dadosbelem.txt', 'r')
for i, line in enumerate(f):
    t.append(datetime.strptime(" ".join(line.split()[:2]), "%d/%m/%Y %H:%M"))
    heights.append(0.01*float(line.split()[2]))
f.close()

print("*******PREVISÃO DE MARÉS PARA BELÉM*********")
ano = input("Digite o Ano que você deseja a tábua de maré\n")
mes = input("Digite o número do mês de "+str(ano)+" que você deseja a tábua de maré\n")
dia = input("Digite qual dia do mês que você deseja a tábua de maré\n")

print("Carregando gráfico de maré...")
##Prepare a list of datetimes, each 6 minutes apart, for a week.

start_date = datetime(int(ano),int(mes),int(dia))
end_date = start_date + relativedelta(days=1) #Mudei para 0, estava days=1
end_date = end_date.replace(hour=0, minute=0, second=0, microsecond=0)
times = date_range(start_date, end_date, 1, 'hours') #Aqui você muda o intervalo de horas


##Fit the tidal data to the harmonic model using Pytides
my_tide = Tide.decompose(heights, t)


##Predict the tides using the Pytides model.
my_prediction = my_tide.at(times)


##Plot the results
plt.figure(figsize=(100,4))
plt.plot(times, my_prediction, label="Pytides")
plt.grid()
plt.title('Previsão de Correntes de Maré para Belém de '+str(start_date)+' até '+str(end_date))
plt.xlabel('Mês-Dia e Hora ')
plt.ylabel('Metros')
plt.show()