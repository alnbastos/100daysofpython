"""
(17/02/2021) Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a
velocidade média esperada para a viagem.
"""
print('CÁLCULE DE TEMPO PARA VIAGEM DE CARRO')
distancia = float(input('Insira a distância a percorrer (em km): '))
velocidade = float(input('Insira a velocidade média esperada (em km/h): '))

tempo = distancia / velocidade

print(f'O tempo médio desta viagem é de {tempo} hora(s).')
