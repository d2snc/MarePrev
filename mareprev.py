#Importo as bibliotecas necessárias para o programa funcionar

from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import tkcalendar
from datetime import timedelta
from datetime import datetime
from pytides.tide import Tide
import numpy as np
import matplotlib.pyplot as plt
from dateutil.relativedelta import relativedelta

root = Tk(className=' MaréPrev') #Crio a janela do Programa MaréPrev com o nome de 'root' para facilitar na hora de escrever o código
root.geometry("500x400") #Defino as dimensões da janela do programa


def date_dif(start, stop): #Essa função foi retirada da internet, ela dá a diferença entre duas datas
    global dates  # If you want to use this outside of functions
    dates = []
    diff = (stop - start).days
    for i in range(diff + 1):
        day = start + timedelta(days=i)
        dates.append(day)
    if dates:
        print(dates)  # Print it, or even make it global to access it outside this
    else:
        print('Make sure the end date is later than start date')

def date_range(start_date, end_date, increment, period): #Esta função também foi retirada da internet, dá a diferença em horas entre datas
    result = []
    nxt = start_date
    delta = relativedelta(**{period:increment})
    while nxt <= end_date:
        result.append(nxt)
        nxt += delta
    return result

def open_file(startdate,finaldate): #Aqui começa a função principal do programa, ela abre o arquivo e considera uma data inicial e uma data final para fazer a previsão de maré
    heights = [] #Defino a variável que vai conter as alturas de maré retiradas do arquivo
    t = [] #Defino a variável que vai armazenar as datas
    f = askopenfile(mode ='r', filetypes =[('Arquivo txt', '*.txt')]) #Abro o arquivo txt que o usuário selecionou
    for i,line in enumerate(f): #Faço um laço de repetição para fazer uma iteração para cada linha do arquivo
        t.append(datetime.strptime(" ".join(line.split()[:2]), "%d/%m/%Y %H:%M")) #Separo na variável t cada datahora do arquivo
        heights.append(0.01 * float(line.split()[2])) #Adiciono a altura da maré, no caso ela deve estar em centímetros
    start_date = datetime(startdate.year, startdate.month, startdate.day) #seleciona a data inicial
    end_date = datetime(finaldate.year, finaldate.month, finaldate.day)   # seleciona a data final
    if end_date == start_date: #Caso a data final seja igual a inicial, então ele vai adicionar 1 dia no primeiro dia, assim ele só pega a previsão de maré de apenas 1 dia
        end_date = start_date + relativedelta(days=1)
    times = date_range(start_date, end_date, 1, 'hours')  # Aqui você muda o intervalo de horas
    my_tide = Tide.decompose(heights, t) #Usando o modelo do pytide para achar o harmônico
    my_prediction = my_tide.at(times) #Faço a predição
    #A partir daqui começa a plotagem do gráfico
    plt.figure(figsize=(25, 15)) #Defino o tamanho do gráfico
    plt.subplot(211) #Uso o subplot para plotar 2 gráficos na mesma imagem
    plt.grid() #Coloco o grid para ter as linhas de referência
    plt.plot(times, my_prediction, label="Pytides") #Ploto a predição que o Pytides me deu
    plt.title('Previsão de Amplitude de Maré para ' + entry1.get() + ' de ' + str(startdate) + ' até ' + str(finaldate)) #Coloco uma legenda na imagem
    plt.xlabel('Mês-Dia e Hora ') #Legenda em x
    plt.ylabel('Metros') #Legenda em y
    #A partir daqui começa a plotagem do histograma
    plt.subplot(212)
    plt.grid()
    plt.hist(my_prediction, bins=20) #Plot o histograma
    plt.title('Histograma de Maré para '+entry1.get())
    plt.xlabel('Altura(m)')
    plt.ylabel('Ocorrências')
    plt.show()

#Aqui para baixo são entradas da GUI, que é a janela que abre para selecionar as coisas
#Escrevo o texto inicial
user_name = Label(root, text = "\n  Este programa realiza a previsão de maré tendo como base um arquivo txt com dados\n  e medições da altura do mar no local desejado.\n\n  O arquivo txt deverá estar com os dados no formato DD/MM/AAAA HH:MM ALTURA \n  por exemplo: 01/01/1963 00:00 202").pack()
user_name = Label(root, text = "\nCaso você queira a maré para apenas 1 dia, deixe a data inicial e a final iguais a esse dia.").pack()
user_name = Label(root, text = "\nDigite o nome do local").pack()
entry1 = Entry(root, width=20) #Recebe o nome do local
entry1.pack()
user_name = Label(root, text = "\nData Inicial da Previsão de Maré").pack()
date1 = tkcalendar.DateEntry(root) #cria o calendário
date1.pack(padx=10, pady=10)
user_name = Label(root, text = "Data Final da Previsão de Maré").pack()
date2 = tkcalendar.DateEntry(root)
date2.pack(padx=10, pady=10)
btn = Button(root, text ='Selecione o Arquivo', command = lambda:open_file(date1.get_date(), date2.get_date())) #Botão executa a ação
btn.pack(side = TOP, pady = 10)
user_name = Label(root, text = "Após selecionar o arquivo aguarde alguns instantes até o gráfico aparecer...").pack()

root.mainloop()



