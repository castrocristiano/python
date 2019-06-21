# -*- coding:utf-8 -*-
x = 2
y = 3
z = 5

print(x == y)
print(x < y)

#Operadores relacionais
soma = x + y
print(soma)
print(soma == x)
print(soma == y)
print(soma > x)
print(soma > y)
print(soma < x)
print(soma < y)
print(soma >= y)
print(soma <= y)
print(soma >= x)
print(soma <= x)

"""
Operadores lógicos
AND
OR
NOT
"""
print("============ Operadores lógicos ============")
print(x == y and x == soma)
print(x == y or soma == z)
print(x == y or soma == z and 2 == soma - y)

# Bloco
print("============  Blocos (identação)  ============")
x = 1
y = 100

if x > y:
    print("x é maior que y")

if y > x:
    print("y é maior que x")

if x > y:
    print("x é maior que y")
else:
    print("x não é maior que y")

# Tabulação

print("============  Tribulação digo, tabulação  ============")
a = 7
b = 6

if b > a:
    if b > 0:
        print("b é marior que a\nb é positivo")
    else:
        print("b não é maior nem positivo")
else:
    print("b é menor que a")

x = 1
y = 2

# elif
print("============  elif  ============")
if x == y:
    print("numeros iguais")
elif y > x:
    print("y maior que x")
else: 
    print("numeros diferentes")


