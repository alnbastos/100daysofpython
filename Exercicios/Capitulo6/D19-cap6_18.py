"""
(23/04/2021) Escreva um programa que gere um dicionário, em que cada chave seja um caractere, e seu valor seja o
número desse caractere encontrado em uma frase lida.
Ex: O rato -> {'O': 1, 'r': 1, 'a': 1, 't': 1, 'o': 1}
"""
import re

frase = str(input('Frase: ')).replace(' ', '')
dicionario = {}

for letra in frase:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
print(dicionario)

"""
Alternativa de solução, utilizando o método get do dicionário.

for letra in frase:
    # Se letra não existir no dicionário, retorna 0
    # se existir, retorna o valor anterior
    dicionario[letra] = dicionario.get(letra, 0) + 1
"""