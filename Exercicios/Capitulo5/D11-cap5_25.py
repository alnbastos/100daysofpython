"""
(23/03/2021) Escreva um programa que calcule a raiz quadrada de um número.
"""
n = int(input('Raiz quadrada de: '))
b = 2
p = 0

#abs - valor absoluto
while abs(n - (b * b)) / 2 > 0.00001:
    p = (b + (n / b)) / 2
    b = p
print(f'A raiz quadrada de {n} é ~{p:.4f}')
