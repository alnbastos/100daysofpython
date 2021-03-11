"""
(10/03/2021) Escreva um programa que pergunte o valor inicial de uma dívida e o juro mensal. Pergunte também o valor
mensal que será pago. Imprima o número de meses para que a dívida seja paga, o total pago e o total de juros pago.
"""
divida_inicial = float(input('Divida inicial: R$'))
taxa = float(input('Juros (Ex: 1 para 1%): '))
pagamento_mensal = float(input('Valor pago mensalmente: R$'))
mes = 1
print()

if divida_inicial * (taxa/100) > pagamento_mensal:
    print('Erro! Os juros são superiores ao pagamento mensal.')
else:
    juros_pago = 0
    total = divida_inicial
    while total > pagamento_mensal:
        juros = total * taxa / 100
        total = total + juros - pagamento_mensal
        juros_pago += juros
        print(f'{mes} mês - Dívida: R${total:.2f}')
        mes += 1

print(f'\nDívida: R${divida_inicial:.2f}. Juros: {taxa:.2f}%')
print(f'Meses a pagar: {mes-1}. Total de juros por mes: R${juros_pago:.2f}')
print(f"No último mês, você terá uma dívida restante de R${total:.2f} a pagar.")
