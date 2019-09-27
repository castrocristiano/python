# -*- coding:utf-8 -*-
a = "Cristiano"
b = "Castro"
concatenada = a + " " + b + '\n' # apenas para demonstrar a utilização do apostrofe ' em strings
print(concatenada)


tamanho = len(concatenada)# length da string

print(tamanho)
print(a[2])


#Imprimindo parte de uma string

print(concatenada[0 : 9])
print(concatenada[ : 9])
print(concatenada[10 : ])

print(concatenada.lower())
print(concatenada.upper())

print(concatenada.strip())

minha_string = 'O rato roeu a roupa do rei de Roma'
minha_lista = minha_string.split(" ")

print(minha_lista)

#buscas de substrings
busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:])

print(minha_string.replace("o rei", "a rainha"))