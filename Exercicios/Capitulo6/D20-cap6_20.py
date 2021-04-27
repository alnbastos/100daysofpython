"""
(26/04/2021) Escreva um programa que compare duas listas. Considere a primeira lista com a versão inicial e a segunda
como a versão após alterações. Utilizando operações com conjuntos, seu programa deverá imprimir a lista de modificações
entre essas duas versões, listando:
* os elementos que não mudaram
* os novos elementos
* os elementos que foram removidos
"""
antes = [0, 1, 2, 3, -1]
depois = [2, 3, 4]

conjunto_antes = set(antes)
conjunto_depois = set(depois)

print('Antes:', antes)
print('Depois:', depois)
print('Elementos que não mudaram:', conjunto_antes & conjunto_depois)
print('Novos elementos:', conjunto_depois - conjunto_antes)
print('Elementos removidos:', conjunto_antes - conjunto_depois)