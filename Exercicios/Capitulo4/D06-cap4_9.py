"""
(24/02/2021) Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar
o valor da casa a compra, o salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser superior a
30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.
"""
print('CALCULO DE EMPRÉSTIMO BANCÁRIO')
valor_casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
quant_anos = int(input('Informe a quantidade de anos a pagar: '))

prestacao = valor_casa / (quant_anos * 12)
minimo_parcela = salario * 0.3

print('-'*20)
print(f'Casa: R${valor_casa:.2f}\n'
      f'Salário: R${salario:.2f}\n'
      f'Anos a pagar: {quant_anos}\n'
      f'Prestação: R${prestacao:.2f}')

if prestacao <= minimo_parcela:
    print('\033[32mEmpréstimo APROVADO.\033[m')
else:
    print('\033[31mEmpréstimo NEGADO.\033[m')
