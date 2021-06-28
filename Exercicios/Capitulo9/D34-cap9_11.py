"""
(28/06/2021) Crie um programa que leia um arquivo e crie um dicionario em que cada chave `e uma palavra e cada valor `e o numero de ocorrencias no arquivo.
"""
import sys

if len(sys.argv) != 2:
    print('Modo de uso: D34-cap9_11.py arquivo1')
    sys.exit(1)

nome_arquivo = sys.argv[1]
contador = {}

arquivo = open(f'arquivos//{nome_arquivo}', 'r', encoding='utf-8')
for linha in arquivo:
    linha = linha.strip().lower()
    palavras = linha.split() # um elemento por lista, ['1'] ['2']...
    for p in palavras:
        if p in contador:
            contador[p] += 1
        else:
            contador[p] = 1
arquivo.close()

for chave in contador:
    print(f'{chave} = {contador[chave]}')

