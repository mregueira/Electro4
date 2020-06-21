import matplotlib.pyplot as plt
import numpy as np
import csv

x1 = []
y1 = []

x2 = []
y2 = []

x3 = []
y3 = []

fileName="C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\d\\Ej2"
saveFiles=True

with open('C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\d\\2dvi33.csv', "r") as csvfile: #aca cargo los datos de una curva en x e y
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x1.append(float(row[0]))
        y1.append(float(row[1]))

with open('C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\d\\2dvi66.csv', 'r') as csvfile:#aca empieza otra curva
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x2.append(float(row[0]))
        y2.append(float(row[1]))

with open('C:\\Users\\marth\\Documents\\ITBA\\Eda\\Electro4\\TP3\\Simulacion\\Ej 2\\comparaciones\\d\\2dvi81.csv', 'r') as csvfile:  # aca empieza otra curva
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x3.append(float(row[0]))
        y3.append(float(row[1]))

#with open('22k.txt', 'r') as csvfile:#aca empieza otra curva
 #   plots = csv.reader(csvfile, delimiter='\t')
 #   for row in plots:
    #    x3.append(float(row[0]))
     #   y3.append(float(row[1]))

#plt.figure()
#plt.subplot(221)
#plt.plot(x1, y1)

#plt.subplot(222)
#plt.plot(x2, y2) esto plotea cuartos
#plt.show() con 211 y 212 plotea dos, uno abajo del otro

#plt.subplot(223)
#plt.plot(x3, y3)

#plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                   # wspace=0.35)


#plt.savefig(fileName+"_1k_10k_22k_V2"+".png")

#plt.show()



fig, axs = plt.subplots(3, 1, sharex=True)
# Remove horizontal space between axes
fig.subplots_adjust(hspace=0.1)

# Plot each graph, and manually set the y tick values
axs[0].plot(x1, y1, label='mf=33', color='cyan', linewidth=1.3)
#axs[0].set_title('Tensión para diferentes valores de R')
axs[0].set_title('Comparación de tensiones con ma=1.1')
axs[0].set_xlim([0,0.025])
axs[0].legend()
#axs[0].set_yticks(np.arange(-0.9, 1.0, 0.4))
#axs[0].set_ylim(-1, 1)

axs[1].plot(x2, y2, label='mf=66', color='magenta', linewidth=1.3)
axs[1].set_ylabel('V')
axs[1].legend()
#axs[1].set_yticks(np.arange(0.1, 1.0, 0.2))
#axs[1].set_ylim(0, 1)

axs[2].plot(x3, y3, label='mf=81', color='darkorange', linewidth=1.3)
axs[2].set_xlabel('t(s)')
axs[2].legend()
#axs[2].set_yticks(np.arange(-0.9, 1.0, 0.4))
#axs[2].set_ylim(-1, 1)


plt.savefig(fileName+"d_V"+".png")

plt.show()
