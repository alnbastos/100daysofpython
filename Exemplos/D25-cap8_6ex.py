#(04/05/2021) Exemplo 8.6 - Funcao modificada para facilitar o rastreamentol

def fatorial(n):
    print('Calculando o fatorial de', n)
    if n == 0 or n == 1:
        print(f'Fatorial de {n} = 1')
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f' fatorial de {n} = {fat}')
    return fat

fatorial(4)

