"""
(27/06/2021) Crie um programa que receba uma lista de nomes de um arquivo e os imprima, um por um.
"""
import sys

if len(sys.argv) < 2:
    print('Como usar: D34-cap9_.py arquivo1 [arquivo2 arquivo3 arquivoN]')
    sys.exit(1)

for nome in sys.argv[1:]:
    try:
        with open(f'arquivos//{nome}.txt', 'r') as arquivo:
            for linha in arquivo:
                print(linha)
    except FileNotFoundError:
        print(f'Arquivo {nome} nao encontrado.')

