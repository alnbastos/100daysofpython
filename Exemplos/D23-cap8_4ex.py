# Exemplo 8.4 - Outra forma de calcular o fatorial
def fatorial(n):
    fat = 1
    x = 1
    while x <= n:
        fat *= x
        x += 1
    return fat

print('Fatorial de 10:', fatorial(10))
print('Fatorial de 5:', fatorial(5))
print('Fatorial de 0:', fatorial(0))
