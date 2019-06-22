'''
media, mediana, moda

media = somar todos os números e dividir pela quantidade de elementos
mediana = ordenar a lista, pegar os números do meio da lista e fazer a média
moda = o número que mais se repete


== Utilizando a API do Python ==
from statistics import *

lista = geraListaAleatoriaInt()

media = mean(lista)
mediana = median(lista)
moda = mode(lista)

'''

def media(lista):
    #media = mean(lista)
    soma = sum(lista)
    quantidadeDeItens = len(lista)
    media = soma / float(quantidadeDeItens)
    return media

def mediana(lista):
    # mediana = median(lista)
    listaOrdenada = sorted(lista)
    t = len(listaOrdenada)

    if t % 2 == 0:
        mediana = (listaOrdenada[int(t / 2)] + listaOrdenada[int(t / 2 - 1)]) / 2
    elif t % 2 == 1:
        mediana = listaOrdenada[int(t/2)]

    return mediana

def moda(lista):
    # moda = mode(lista)
    
    listaDic = {}

    for l in lista:
        if l not in listaDic:
            listaDic[l] = 1
        else:
            listaDic[l] += 1 

    maiorRepeticao = max(listaDic.values())

    for i in listaDic:
        if listaDic[i] == maiorRepeticao:
            moda = i

    return moda