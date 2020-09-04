import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint, shuffle
import timeit
import random

def plot_grafico(x, y, file_name, label1, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label= label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)

    fig.savefig(file_name)

def geraLista(tam):
    lista = list(range(1, tam+1))
    shuffle(lista)
    return lista
    
def particao(lista, ini, fim):
    pivo = lista[fim - 1]
    for i in range(ini, fim):
        if not lista[i] > pivo:
            lista[ini], lista[i] = lista[i], lista[ini]
            ini += 1
    return ini-1

def escolhe_pivo_aleatorio(lista, ini, fim):
    rand = random.randrange(ini, fim)
    lista[fim - 1], lista[rand] = lista[rand], lista[fim - 1]
    return particao(lista, ini, fim)

#Merge Sort
def algoritmo(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]
        algoritmo(esquerda)
        algoritmo(direita)

        i = 0
        j = 0
        k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1



x =  [20000,40000,60000,80000,100000]
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
    tempo_aleatorio.append(timeit.timeit("algoritmo({}, {}, {})".format(y_aleatorio[i], 0, x[i] - 1), setup="from __main__ import algoritmo", number=1))

plot_grafico(x, tempo_aleatorio, "grafico.png", "Tempo")
