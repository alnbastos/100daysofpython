"""
(17/02/2021) Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de
cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro e
calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
"""
print('CÁLCULO DE DIAS FUMANTE')

quantidade_cigarro = int(input('Quantos cigarros fuma por dia? '))
quantidade_anos = int(input('Quantos anos fuma cigarro? '))

min_cigarro = (quantidade_cigarro * 10) * (365 * quantidade_anos)
dias_cigarro = min_cigarro / (60 * 24)  # 60min em 24 horas

print(f'Por causa do cigarro, você perdeu {dias_cigarro:.0f} dias.')
