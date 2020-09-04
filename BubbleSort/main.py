# BubbleSort
from random import randint
import timeit
import matplotlib as mpl
import timeit
from random import randint
import matplotlib.pyplot as plt

def bubbleSort(lista):
    contador = 0
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            contador+=1
            if lista[j] > lista[j+1] :
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return contador

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,BSort,xl = "Entradas", yl = "loops",nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,BSort, label = "Bubble Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)


  
lista = [1000,10000,30000,60000]
saida_1 = []
saida_2 = []


for i in range(len(lista)):
  saida_1.append(timeit.timeit("bubbleSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,bubbleSort",number=1))

desenhaGrafico(lista,saida_1,nam="tempo")

for i in range(len(lista)):

  saida_2.append(bubbleSort(geraLista(lista[i])))

desenhaGrafico(lista,saida_2,nam="grafico")
