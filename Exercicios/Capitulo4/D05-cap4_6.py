"""
(24/02/2021) Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
Calcule o preço da passagem, cobrando R$0.50 por km para passagens de até 200km, e R$0.45 para viagens mais longas.
"""
distancia = float(input('Insira a distância que deseja percorrer, em KM: '))

if distancia <= 200:
    cobrar = distancia * 0.50
else:
    cobrar = distancia * 0.45

print(f'Com uma viagem de {distancia} KM, você pagará R${cobrar:.2f}')
