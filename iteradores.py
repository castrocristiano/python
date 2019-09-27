# -*- coding:utf-8 -*-
x = 1

while x < 10:
    print(x)
    x += 1
    #x = x + 1

print("=========  for  ==========")

lista1 = [1,2,3,4,5,6,7,8,9]
lista2 = ["ola", "mundo", "!"]
lista3 = [0, "0", "ola", 9.99, True]

for i in lista1:
    print(i)

for i in lista2:
    print(i)

for i in lista3:
    print(i)

print("=========  Range  ==========")

print("=========  Range 10  ==========")
for i in range(10):
    print(i)

print("=========  Range 10 até 20  ==========")
for i in range(10, 20):
    print(i)

print("=========  Range 10 até 20 de 2 em 2  ==========")
for i in range(10, 20, 2):
    print(i)