# (22/06/2021) processamento de um arquivo
largura = 79
with open('Cap9_arquivos//entrada_ex5.txt') as entrada:
    for linha in entrada.readlines():
        if linha[0] == ';':
            continue
        elif linha[0] == '>':
            print(linha[1:].rjust(largura))
        elif linha[0] == '*':
            print(linha[1:].center(largura))
        else:
            print(linha)
