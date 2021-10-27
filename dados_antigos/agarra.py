# importing tkinter and tkinter.ttk
# and all their functions and classes
from tkinter import *




#Código original
plt.figure()
plt.subplot(211)
plt.figure(figsize=(100, 4))
plt.plot(times, my_prediction, label="Pytides")
plt.grid()
plt.title('Previsão de Correntes de Maré para ' + entry1.get() + ' de ' + str(startdate) + ' até ' + str(finaldate))
plt.xlabel('Mês-Dia e Hora ')
plt.ylabel('Metros')

plt.subplot(212)  # Aqui vou plotar o gráfico do histograma
plt.hist(my_prediction, bins=25)
plt.title('Nível do Mar - Belém - 1963-1967 - Frequência')
plt.xlabel('Altura(m)')
plt.ylabel('Ocorrências')