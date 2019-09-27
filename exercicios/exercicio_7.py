print('Sequencia de Fibonacci')

def fibonacci(num):
    n = int(num)
    a = 0
    b = 1
    print(a)
    while (b < n):
        c = a
        a = b
        b = a + c
        print(a)

fibonacci(input('Digite um número: '))

