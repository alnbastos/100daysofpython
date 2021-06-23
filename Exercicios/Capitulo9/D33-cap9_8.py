"""
(22/06/2021) Modifique o programa 9.7 para também receber o número de caracteres por linha e o número de linhas por
página pela linha de comando.
"""
import sys


def verifica_pagina(arquivo, linha, pagina):
    if linha == LINHAS:
        rodape = f"= {NOME_DO_ARQUIVO} - Página: {pagina} ="
        arquivo.write(rodape.center(LARGURA - 1) + "\n")
        pagina += 1
        linha = 1
    return linha, pagina


def escreve(arquivo, linha, nlinhas, pagina):
    arquivo.write(linha + "\n")
    return verifica_pagina(arquivo, nlinhas + 1, pagina)


if len(sys.argv) != 3:
    print('Como usar: D33-cap9_8.py largura linhas')
    sys.exit(1)

LARGURA = int(sys.argv[1])
LINHAS = int(sys.argv[2])
NOME_DO_ARQUIVO = "arquivos//mobydick_ex7.txt"

entrada = open(NOME_DO_ARQUIVO, encoding="utf-8")
saida = open("arquivos//saida_paginada_ex8.txt", "w", encoding="utf-8")

pagina = 1
linhas = 1

for linha in entrada.readlines():
    palavras = linha.rstrip().split(" ")
    linha = ""
    for p in palavras:
        p = p.strip()
        if len(linha) + len(p) + 1 > LARGURA:
            linhas, pagina = escreve(saida, linha, linhas, pagina)
            linha = ""
        linha += p + " "
    if linha != "":
        linhas, pagina = escreve(saida, linha, linhas, pagina)

while linhas != 1:
    linhas, pagina = escreve(saida, "", linhas, pagina)

entrada.close()
saida.close()
