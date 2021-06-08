"""
(07/06/2021) Utilizando a função type, escreva uma função recursiva que imprima os elementos de uma lista. Cada elemento
deve ser impresso separadamente, um por linha. Considere o caso de listas dentro de listas, como L = [1, [2, 3, 4, [5,
6, 7]]]. A cada nível, imprima a lista mais à direita, como fazemos para identar blocos em Python. Dica: envie o nível
atual como parâmetro e utilize-o para calcular a quantidade de espaços em branco à esquerdade cada elemento.
"""
espacos_por_nivel = 4


def imprime_elementos(lista, nivel=0):
    espacos = ' ' * espacos_por_nivel * nivel
    if type(lista) is list:
        print(espacos, '[')
        for elemento in lista:
            imprime_elementos(elemento, nivel+1)
        print(espacos, ']')
    else:
        print(espacos, lista)


L = [1, [2, 3, 4, [5, 6, 7]]]
imprime_elementos(L)
