import matplotlib.pyplot as plt
import numpy as np
import csv

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

fileName="C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\b\\Ej2"
saveFiles=True

from distutils.spawn import find_executable

with open('C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\b\\2bvi08.csv', 'r') as csvfile: #aca cargo los datos de una curva en x e y
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))
        y1.append(float(row[2]))

with open('C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\b\\2bvi1.csv', 'r') as csvfile:  # aca empieza otra curva
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(float(row[0]))
        y2.append(float(row[2]))


with open('C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\b\\2bvi13.csv', 'r') as csvfile:#aca empieza otra curva
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x3.append(float(row[0]))
        y3.append(float(row[2]))

#grafico 1

fig, graph1 = plt.subplots() #todo lo escrito en el grafico se configura aca
#graph1.set_ylim([-100,20])
graph1.set_xlim([0,0.025])
graph1.set_xlabel('t')
graph1.set_ylabel('I')
graph1.set_title('Corriente con ma=0.8')
graph1.grid()
#graph1.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
#graph1.set_xscale('log')
graph1.plot(x1,y1,color='cyan', linewidth=1.3, label='ma=0.8', linestyle='dashed')  # plot vgs
#graph1.tick_params(axis='y', labelcolor='r')#esto es para el color de los numeritos
graph1.legend(loc=('upper left'))


#grafico 2
graph2 = graph1#.twinx() #esto es para hacer una escala diferente para cada plot
#graph2.set_ylim([-2.5,1])
#graph2.set_ylabel('dB')
#graph2.tick_params(axis='y', labelcolor='b')
graph2.plot(x2,y2,label='ma=1', color='magenta', linewidth=1.3, linestyle='dashed')
graph2.legend(loc='upper left')


#grafico 3
graph3 = graph2
#graph3.set_ylim([-2.5,1])
#graph3.set_ylabel('dB')
#graph3.tick_params(axis='y', labelcolor='g')
graph3.plot(x3,y3,label='ma=1.3', color='darkorange', linewidth=1.3, linestyle='dashed')
graph3.legend(loc='upper left')



if saveFiles:#si quiero guardar el archivo, lo guardo
    plt.savefig(fileName+"b_I"+".png")
plt.show()