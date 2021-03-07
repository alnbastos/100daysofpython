"""
(17/02/2021) Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
"""
print('ALUGUEL DE CARRO')
km_percorrido = float(input('Insira os KM percorridos: '))
dias_alugado = int(input('Quantidade de dia(s) alugado: '))

total_pagar = (km_percorrido * 0.15) + (dias_alugado * 60)

print(f'Total a pagar: R${total_pagar:.2f}')
