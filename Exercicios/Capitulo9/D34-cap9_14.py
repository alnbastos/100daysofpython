"""
(28/06/2021) Crie um programa que leia um arquivo-texto e elimine os espacos repetidos entre as palavras e no fim das linhas. O arquivo de saida tambem nao deve ter mais de uma linha em branco repetida.
"""
import sys

if len(sys.argv) != 3:
    print('Modo de uso: D34-cap9_14.py arquivo_entrada arquivo_saida')
    sys.exit(1)

entrada = sys.argv[1]
saida = sys.argv[2]
branco = 0

with open(f'arquivos//{entrada}', 'r') as arquivo_entrada, open(f'arquivos//{saida}', 'w') as arquivo_saida:
    for linha in arquivo_entrada:
        linha = linha.rstrip() # remove espacos a direita
        linha = linha.replace('  ', '') # remove espacos repetidos
        if linha == '':
            branco += 1
        else:
            branco = 0

        if branco < 2: # nao escreve a partir da segunda linha em branco
            arquivo_saida.write(linha+'\n')

