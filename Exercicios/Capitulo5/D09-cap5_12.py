"""
(10/03/2021) Altere o programa anterior de forma a perguntar também o valor depositado mensalmente. Esse valor será
depositado no início de cada mês, e você deve considerá-lo para cálculo de juros do mês seguinte.
"""
deposito_inicial = float(input('Depósito inicial: R$'))
juros = float(input('Juros (Ex: 1 para 1%): '))
deposito_mensal = float(input(f'Depósito mensal: R$'))

mes = 1
total = deposito_inicial

while mes <= 24:
    total += total * (juros/100) + deposito_mensal
    print(f'{mes} mês - R${total:.2f}')
    mes += 1
print(f"O ganho obtido com os juros foi de R${total-deposito_inicial:8.2f}.")
