#(04/05/2021) Exemplo 8.5 - Funcao recursiva do fatorial

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

