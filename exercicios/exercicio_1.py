'''
Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.    
'''

def isMaiorDeIdade(idade):
    return int(idade) >= 18

def lerIdade():
    idade = input("Digite sua idade: ")
    return idade

if isMaiorDeIdade(lerIdade()):
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")