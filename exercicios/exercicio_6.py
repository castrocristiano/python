print('Fatorial')

def fatorial(num):
    n = int(num)
    if n == 0:
        return 1
    else:
        return n * fatorial(n -1)

numero = input("Digite um número: ")

print("Fatorial = ", fatorial(numero))