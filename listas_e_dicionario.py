# -*- coding: utf-8 -*-
minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [1,2,3,4,5]
minha_lista_3 = ["abacaxi", 2, 9.23, True]
minha_lista_4 = []

minha_lista_4.append(57)
print(minha_lista_4)
print(minha_lista_3)

print(minha_lista)
print(minha_lista[1])

for fruta in minha_lista:
    print(fruta)

print("Tamanho da lista: ", len(minha_lista))
limao = "limão"
minha_lista.append(limao)

print(minha_lista)

# checando se um item está contido na minha lista

if 7 not in minha_lista_2:
    print("7 não está na lista")

if 3 in minha_lista_2:
    print(3, "está na minha lista")

if limao in minha_lista:
    print(limao, "está na minha lista")

print(minha_lista_2)
del minha_lista_2 [2:]
print(minha_lista_2)

# ordenação de listas
print("\n\n\nordenação de listas\n")

lista = [124,345, 72,5,46,6,7,3,1,7,0]

lista_ordenada = sorted(lista)

lista.sort(reverse = True)

print(lista)
print(lista_ordenada)

lista_ordenada.reverse()
print(lista_ordenada)

minha_lista.sort()
print(minha_lista)

minha_lista.sort(reverse = True)
print(minha_lista)

# Dicionários
print("\n\n\nDicionários\n")

emails = {"Cristiano": "cristiano@gmail.com", "Cristiano Live": "cristiano@live.com"}
print(emails)
print(emails["Cristiano"])

print("Laço for no dicionário\n")
for k in emails:
    print(emails[k])

