# (11/05/2021) - Funcoes como parametro
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def imprime(a, b, fober):
    print(fober(a, b))

imprime(5, 4, soma)
imprime(10, 1, subtracao)

