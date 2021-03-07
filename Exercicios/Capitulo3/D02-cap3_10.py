"""
(17/02/2021) Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem
do aumento. Exiba o valor do aumento e do novo salário.
"""
print('\033[32mCÁLCULO DO AUMENTO DE SALÁRIO\033[m')
salario = float(input('Salário: R$'))
porcentagem = float(input('Porcentagem (sem %): '))

aumento = salario * (porcentagem / 100)
novo_salario = salario + aumento

print(f'Você teve um aumento de \033[32mR${aumento:.2f}\033[m,'
      f' totalizando \033[32mR${novo_salario:.2f}\033[m no novo salário.')
