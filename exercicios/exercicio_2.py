'''
Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.  
'''
def lerNota():
    nota = input("Digite sua nota:")
    return nota

def mensagemAprovado(nota):
    if int(nota) >= 6:
        return "Aprovado."
    else:
        return "Reprovado."

print(mensagemAprovado(lerNota()))
print(mensagemAprovado(lerNota()))
