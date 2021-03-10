"""
(02/03/2021) Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo, assim como
o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado. Lembre-se de que podemos
entender o quociente da divisão de dois números como a quantidade de vezes que podemos retirar o divisor do dividendo.
Logo, 20/4=5, uma vez que podemos subtrair 4 cinco vezes de 20.
"""
print('--- DIVISÃO COM SUBTRAÇÃO ---')
dividendo = int(input('Dividendo: '))
divisor = int(input('Divisor: '))

cont = dividendo
resultado = 0
while cont >= divisor:
    cont -= divisor
    resultado += 1

resto = cont
print(f'{dividendo} / {divisor} = {resultado}')
print(f'Resto: {resto}')
