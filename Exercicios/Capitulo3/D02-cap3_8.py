"""
(17/02/2021) Escreva um programa que leia um valor em metros e o exiba convertidos em milímetros.
"""
print('\033[35mCONVERSÃO DE METROS PARA MILÍMETROS\033[m')

metro = float(input('Insira o valor do metro: '))
mili = metro * 1000

print(f'{metro} m = {mili} mm')
