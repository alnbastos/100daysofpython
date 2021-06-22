"""
(22/06/2021) Modifique o programa do Exercicio 9.1 para que receba mais dois parametros: a linha de inicio e a de fim para impressao.
O programa deve imprimir apenas as linhas entre esses dois valores(incluindo as linhas de inicio e fim).
"""
import sys

if len(sys.argv) != 4:
    print('Como usar: D33-cap9_2.py nome_arquivo num_inicio num_fim')
else:
    try:
        nome_arquivo = sys.argv[1]
        num_inicio = int(sys.argv[2])
        num_fim = int(sys.argv[3])
        with open(f'arquivos//{nome_arquivo}', 'r') as arquivo:
            for linha in arquivo.readlines()[num_inicio-1:num_fim]:
                print(linha[:-1]) #retira a linha que contem o enter
    except FileNotFoundError:
        print(f'Arquivo {nome_arquivo} nao encontrado.')

