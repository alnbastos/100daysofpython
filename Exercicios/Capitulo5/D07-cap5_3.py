"""
(27/02/2021) Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir
10, 9, 8,..., 1, 0 e Fogo! na tela.
"""
import time, emoji
x = 10
while x >= 0:
    print(x, end=', ')
    x -= 1
    time.sleep(1)

print(emoji.emojize('Fogo!:rocket:'))
