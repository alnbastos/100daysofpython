# (21/06/2021) Utilizando o with
with open('Cap9_arquivos//D32-cap9_numeros.txt', 'r') as arquivo:
    for linha in arquivo.readlines():
        print(linha)
