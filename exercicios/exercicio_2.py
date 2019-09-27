'''
Faça um programa que receba duas notas digitadas pelo usuário. Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.  
'''
def lerNota():
    nota = input("Digite sua nota:")
    return float(nota)

def mensagemAprovado(notaA, notaB):
    media = (notaA + notaB) / 2
    print("Sua média é %f" %media)
    if float(media) >= 6:
        return "Aprovado."
    else:
        return "Reprovado."
notaA = lerNota()
notaB = lerNota()

print(mensagemAprovado(notaA, notaB))
