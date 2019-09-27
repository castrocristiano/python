'''
Escreva um programa que ordene uma lista numérica com três elementos.    
'''

lista = []

for i in range(0, 3):
    valor = input("Digite um número:")
    lista.append(valor)

def selection_sort(l):
    
    for i in range(len(l)):
        menor = i
        for j in range(i + 1, len(lista)):
            if l[j] < l[menor]:
                menor = j
        if l[i] != l[menor]:
            aux = l[i]
            l[i] = l[menor]
            l[menor] = aux
    return l

print('lista = ', lista)
print('lista ordenada = ',selection_sort(lista))


listaOrdenada = lista.sort()
print(listaOrdenada)