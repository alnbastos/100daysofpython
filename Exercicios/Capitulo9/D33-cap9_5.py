"""
(22/06/2021) Crie um programa que inverta a ordem das linhas do arquivo pares_ex3.txt.
A primeira linha deve conter o maior numero; e a ultima, o menor.
"""
pares = open('arquivos//pares_ex3.txt', 'r')
saida = open('arquivos//pares_invertidos_ex5.txt', 'w')

linha_par = pares.readlines()
linha_par.reverse()

for linha in linha_par:
    saida.write(linha)

pares.close()
saida.close()
