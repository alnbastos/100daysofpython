"""
(22/06/2021) Crie um programa que receba o nome de dois arquivos como parametros da linha de comando e que gere
um arquivo de saida com as linhas do primeiro e segundo arquivo.
"""
import sys

if len(sys.argv) != 4:
    print('Como usar: D33-cap4.py arquivo_um arquivo_dois arquivo_saida')

else:
    try:
        primeiro = open(f'arquivos//{sys.argv[1]}', 'r')
        segundo = open(f'arquivos//{sys.argv[2]}', 'r')
        saida = open(f'arquivos//{sys.argv[3]}','w')
        
        for linha_primeiro in primeiro:
            saida.write(linha_primeiro)
        for linha_segundo in segundo:
            saida.write(linha_segundo)

        primeiro.close()
        segundo.close()
        saida.close()
    except FileNotFoundError:
        print('Arquivos nao encontrados.')

