# -*- coding:utf-8 -*-
'''
Funções em Python são definidas pela palavra def
'''
def soma(x, y):
    valorSomado = x + y 
    return valorSomado
def valorMultiplicacao(x, y):
    return x * y

valorSomado = soma(2,3)
print(valorSomado)

valorMultiplicacao = valorMultiplicacao(5,3)
print(valorMultiplicacao)

print(soma(valorSomado, valorMultiplicacao))
 