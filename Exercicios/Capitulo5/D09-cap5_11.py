"""
(10/03/2021) Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
Exiba os valores mês a mês para os 24 primeiros meses. Escreva o total ganho com juros no período.
"""
deposito = float(input('Depósito Inicial: R$'))
juros = float(input('Juros (Ex: 1 para 1%): '))

mes = 1
total = deposito
while mes <= 24:
    total += total * (juros/100)   # incrementa o deposito com juros
    print(f'{mes} mês - R${total:.2f}')
    mes += 1

print(f'O ganho obtido com os juros foi de R${total-deposito:.2f}')
