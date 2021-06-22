"""
(22/06/2021) Escreva um programa que receba o nome de um arquivo pela linha de comando e que imprima todas as linhas desse arquivo.
"""
import sys

if len(sys.argv) != 2:
    print('\nComo usar: D33-cap9_1.py nome_arquivo\n\n')
else:
    try:
        nome_arquivo = sys.argv[1]
        with open(f'arquivos//{nome_arquivo}', 'r') as arquivo:
            for linha in arquivo.readlines():
                print(linha[:-1])
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} nao encontrado.')

