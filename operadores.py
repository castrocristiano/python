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
