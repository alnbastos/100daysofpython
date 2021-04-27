"""
(26/04/2021) Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
* os valores comuns às duas listas
* os valores que só existem na primeira
* os valos que existem apenas na segunda
* uma lista com os elementos não repetidos das duas listas
* a primeira lista sem os elementos repetidos na segunda
"""
lista1 = [0, 1, 2, 3, -1]
lista2 = [2, 3, 4]

print('Lista 1:', lista1)
print('Lista 2:', lista2)

primeira = set(lista1)
segunda = set(lista2)

# for para imprimir os valores comuns nas duas listas
# print('Valores comuns nas duas listas: ', end='')
# for x in primeira:
#     if x in segunda:
#         print(x, end=', ')

# Inserção: A & B resulta no conjunto de elementos presentes em A e B
print('Valores comuns nas duas listas', primeira & segunda)

print('Valores existentes na primeira lista:', primeira - segunda)

print('Valores existentes na segunda lista:', segunda - primeira)

# Subtração Simétrica: A ^ B = A - B | B - A
print('Elementos não repetidos das duas listas:', primeira ^ segunda)

print('Elementos não repetidos da primeira para a segunda lista:', primeira | segunda)
