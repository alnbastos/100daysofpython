"""
(28/06/2021) Crie um progrma que imprima as linhas de um arquivo. Esse programa deve receber tres parametros pela linha de comando: o nome do arquivo, a linha inicial e a ultima linha a imprimir.
"""
import sys

if len(sys.argv) <= 3:
    print('Modo de uso: D34-cap9_13.py nome_arquivo linha_inicial linha_final')
    sys.exit(1)

else:
    nome_arquivo = sys.argv[1]
    linha_inicio = int(sys.argv[2])
    linha_fim = int(sys.argv[3])

    try:
        arquivo = open(f'arquivos//{nome_arquivo}', 'r')
        for linha in arquivo.readlines()[linha_inicio-1:linha_fim]:
            print(linha[:-1])
        arquivo.close()
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} nao encontrado')
