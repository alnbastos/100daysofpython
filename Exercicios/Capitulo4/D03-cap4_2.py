"""
(22/02/2021) Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h,
exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa,
cobrando R$5 por km acima de 80km/h.
"""
veloc_carro = float(input('Velocidade do carro em KM/H: '))

if veloc_carro > 80:
    multa = (veloc_carro - 80) * 5
    print(f'MULTADO! você deverá pagar uma multa de R${multa:.2f}')
else:
    print('Continue assim! Respeite o trânsito.')
