'''
Escreva um programa que ordene uma lista numérica com três elementos.    
'''

lista = []

for i in range(0, 3):
    valor = input("Digite um número:")
    lista.append(valor)

def selection_sort(lista):
    
    for i in range(len(lista)):
        menor = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        if lista[i] != lista[menor]:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux


lista.sort()
print(lista)