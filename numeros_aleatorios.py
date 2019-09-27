import random
import listas_e_dicionario

numero = random.randint(0, 10)
print(numero)
'''
 Utilizando uma variável de outro script. 
 Valor da lista: [345, 124, 72, 46, 7, 7, 6, 5, 3, 1, 0]
'''
lista = listas_e_dicionario.lista
print(lista)
escolhido = random.choice(lista)
print(escolhido)

