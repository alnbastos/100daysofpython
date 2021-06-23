"""
(22/06/2021) Modifique o programa 9.5 para imprimir 40 vezes o símbolo de = se este for o primeiro caractere da linha.
Adicione também a opção para parar de imprimir até que se pressione a tecla Enter cada vez que a uma linha inicia com
. (ponto) como primeiro caractere.
"""
largura = 79
with open('arquivos//entrada_ex6.txt') as entrada:
    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(largura))
        elif linha[0] == '*':
            print(linha[1:].center(largura))
        elif linha[0] == '=':
            print('=' * 40)
        elif linha[0] == ".":
            input("Digite algo para continuar: ")
            print()
        else:
            print(linha)
