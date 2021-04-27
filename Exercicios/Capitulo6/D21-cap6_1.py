"""
(27/04/2021) Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a
posição de início.
1 string: AABBEEFAATT 
2 string: BE
Resultado: BE encontrado na posição 3 de AABBEEFAATT
"""
primeira = str(input('Primeira frase: ')).upper()
segunda = str(input('Pesquisar: ')).upper()

posicao = primeira.find(segunda)

if posicao > 0:
    print(f'{segunda} está na posição {posicao} de {primeira}')
else:
    print(f'{segunda} não foi encontrado em {primeira}')
