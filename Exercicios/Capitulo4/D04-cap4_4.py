"""
(23/02/2021) Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salário
superiores a R$1250.00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.
"""
print('CALCULO DE VALOR DE SALÁRIO')
salario = float(input('Insira o salário: R$ '))
base = salario
aumento = 0

if salario > 1250:
    aumento = base + (base * 0.10)

if salario <= 1250:
    aumento = base + (base * 0.15)

print(f'Salário: R${salario:.2f}\nAumento: R${aumento:.2f}')
