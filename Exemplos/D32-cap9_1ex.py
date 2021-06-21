# (21/06/2021) Abrindo, criando, lendo e fechando um arquivo

# escrita do arquivo, com 100 linhas
arquivo = open(r'Cap9_arquivos\D32-cap9_numeros.txt', 'w')
for linha in range(1, 101):
    arquivo.write(f'{linha}\n')
arquivo.close()

# leitura do arquivo anterior
arquivo = open(r'Cap9_arquivos\D32-cap9_numeros.txt', 'r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
