# Utilizando while e contadores, verificando se é par ou impar
fim = int(input('Digite o último número a imprimir: '))
x = 0
print('Pares: ', end='')
while x <= fim:
    if x % 2 == 0:
        print(x, end=' ')
    x += 1

# simplificando o programa anterior
print()
print('-' * 35)
x = 0
print('Pares: ', end='')
while x <= fim:
    print(x, end=' ')
    x += 2
