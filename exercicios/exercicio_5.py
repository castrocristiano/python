'''
Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.    
'''
a = float(input("Digite o primeiro número: "))
operador = input("Digite o operador: ")
b = float(input("Digite o segundo número: "))

if operador == "+":
    resultado = a + b
elif operador == "+":
    resultado = a - b
elif operador == "*":
    resultado = a * b
elif operador == "/":
    if b == 0:
        print("Não é possível dividir por 0")
        resultado = None
    else:
        resultado = a / b
elif operador == "%":
    resultado = a % b
else:
    resultado = 0

print(resultado)