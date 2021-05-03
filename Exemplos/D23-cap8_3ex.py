# Exemplo 8.3 - Calculo de integral

def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat

print('Fatorial de 10:', fatorial(10))
print('Fatorial de 5:', fatorial(5))
print('Fatorial de 0:', fatorial(0))
