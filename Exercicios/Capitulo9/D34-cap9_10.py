"""
(27/06/2021) Crie um programa que receba uma lista de nomes de arquivo e que gere apenas um grande arquivo de saida.
"""
import sys

if len(sys.argv) < 2:
    print('Como usar: D34-cap9_10.py arquivo1 [arquivo2 arquivo3 arquivoN]')
    sys.exit(1) #sair do sys

saida = open('arquivos//saida_ex10.txt', 'w', encoding='utf-8')
for nome in sys.argv[1:]:
    with open(f'arquivos//{nome}.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            saida.write(linha)
saida.close()
