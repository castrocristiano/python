"""
Escreva um programa que resolva uma equação de segundo grau.
"""
import math

def calcularDelta(a, b, c):
    delta = (math.pow(b, 2)) - (4 * (int(a) * int(c)))
    return delta


def bhaskara(a, b, c):
    resultado = {"x1": None, "x2": None}
    delta = calcularDelta(a, b, c)

    if delta < 0 :
        print ("Raiz negativa nao pode ser extraida.")
    else:
        x = math.sqrt(delta)
        x1 = (-b + x) / (2 * a)
        x2 = (-b - x) / (2 * a)
        resultado = {"x1": x1, "x2": x2}
    return resultado

a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

print(bhaskara(a, b, c))
