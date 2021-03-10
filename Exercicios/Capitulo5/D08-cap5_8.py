"""
(02/03/2021) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo.
Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos entender a
multiplicação de dois números como somas sucessivas de um deles. Assim, 4x5 = 5+5+5 = 4+4+4+4+4
"""
print('--- TABUADA SEM MULTIPLICAÇÃO ---')
primeiro = int(input('Tabuada de: '))
segundo = int(input('Multiplicador: '))

print(f'{primeiro} x {segundo} = ', end='')

cont = 1
soma = 0
while cont <= primeiro:
    soma += segundo
    print(segundo, end='')
    print(' = ' if cont >= primeiro else ' + ', end='')
    cont += 1
print(soma)
