"""
(07/06/2021) Altere o exemplos 8.20 de forma que o usuario tenha tres chances de acertar o numero. O programa termina se o usuario acertar ou errar tres vezes.
"""
import random

pontos = 0

for x in range (1, 4):
    numero = random.randint(1, 10)
    escolha = int(input('Escolha um numero entre 1 e 10: '))
    if escolha == numero:
        print('Voce acertou! :D \n')
        pontos += 1
    else:
        print(f'Voce errou. O numero era {numero} \n')

print('Pontuacao final:', pontos)
