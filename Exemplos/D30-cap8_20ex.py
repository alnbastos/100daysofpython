# (07/06/2021) - Adivinhado o numero
import random

n = random.randint(1, 10)
x = int(input('Escolha um numero entre 1 e 10: '))
if x == n:
    print('Voce acertou!')
else:
    print('Voce errou. O numero `e:', n)

