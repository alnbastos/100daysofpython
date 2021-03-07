"""
(17/02/2021) Faça um programa que solicite o preço de uma mercadoria e o percentual de desconto.
Exiba o valor do desconto e o preço a pagar.
"""
print('\033[33mCÁLCULO DE DESCONTO\033[m')
produto = float(input('Preço do produto: R$'))
porc_desconto = float(input('Porcentagem (sem %): '))

desconto = produto * (porc_desconto / 100)
novo_preco = produto - desconto

print(f'O produto teve desconto de \033[33mR${desconto:.2f}\033[m,'
      f' obtendo um novo preço de \033[33mR${novo_preco:.2f}\033[m.')
