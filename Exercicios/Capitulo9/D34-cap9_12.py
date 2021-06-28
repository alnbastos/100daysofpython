"""
(28/06/2021) Modifique o programa do Exercicio 9.11 para tambem registrar a linha e a coluna de cada ocorrencia da palavra no arquivo. Para isso, utilize listas nos valores de cada palavra, guardando a linha e a coluna de cada ocorrencia..
"""
import sys

if len(sys.argv) != 2:
    print('Modo de uso: D34-cap9_12.py arquivo1')
    sys.exit(1)

nome_arquivo = sys.argv[1]
contador = {}
arquivo_linha = 1
arquivo_coluna = 1

arquivo = open(f'arquivos//{nome_arquivo}', 'r', encoding='utf-8')
for linha in arquivo:
    linha = linha.strip().lower()
    palavras = linha.split(' ') # um elemento por lista, considerando os espacos repetidos
    for p in palavras:
        if p == '':
            arquivo_coluna += 1
            continue
        if p in contador:
            contador[p].append((arquivo_linha, arquivo_coluna))
        else:
            contador[p] = [(arquivo_linha, arquivo_coluna)]
        arquivo_coluna += len(p)+1
    arquivo_linha += 1
    arquivo_coluna = 1
arquivo.close()

for chave in contador:
    print(f'{chave} = {contador[chave]}')

