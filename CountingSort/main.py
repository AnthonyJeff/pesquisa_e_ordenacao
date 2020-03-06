import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit

def plot_grafico(x, y, z, file_name, label1, label2, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label= label1)
    ax.plot(x, z, label= label2)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)

    fig.savefig(file_name)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista

#Counting Sort
def algoritmo(lista, maximo):
	count = [0] * (maximo+1)
	listaOrdenada = [None] * len(lista)
	for i in range(len(lista)):
		count[lista[i]] += 1
	for i in range(1, maximo+1):
		count[i] += count[i-1] 
	for i in range(len(lista)):
		listaOrdenada[count[lista[i]]-1] = lista[i]
		count[lista[i]] -= 1
  return count


x = [1000, 20000, 30000, 60000]
#x = [100, 2000, 3000, 6000]
y_aleatorio = []
y_reverso = []
tempo_aleatorio = []
tempo_reverso = []


for i in range(len(x)):
    y_aleatorio.append(geraLista(x[i]))
    lista_reversa = list(range(1, x[i]))
    lista_reversa = lista_reversa[::-1]
    y_reverso.append(lista_reversa)

for i in range(len(x)):
    tempo_aleatorio.append(timeit.timeit("algoritmo({})".format(y_aleatorio[i]), setup="from __main__ import algoritmo", number=1))
    tempo_reverso.append(timeit.timeit("algoritmo({})".format(y_reverso[i]), setup="from __main__ import algoritmo", number=1))

plot_grafico(x, tempo_aleatorio, tempo_reverso, "Grafico.png", "Lista Aleatória", "Lista Invertida")
