"""
(17/02/2021) Escreva um programa que converta uma temperatura digitada em ºC em ºF.
"""
print('CONVERSÃO DE GRAUS PARA FAHRENHEIT')
c = float(input('Insira o valor de Celsius (ºC): '))

f = (9 * c) / 5 + 32

print(f'{c:.2f} ºC  =  {f:.2f} ºF')
