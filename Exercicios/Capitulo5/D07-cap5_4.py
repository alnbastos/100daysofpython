"""
(27/02/2021) Faça um programa imprirmi de 1 até o número digitado pelo usuário, mas apenas os números impares.
"""
fim = int(input('Digite o último número a imprimir: '))
x = 1
while x <= fim:
    if x % 2 == 1:
        print(x)
    x += 1
