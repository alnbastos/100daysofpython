"""
(03/05/2021) Reescreva a funcao do exemplo 8.1 de forma a utilizar os metodo de pesquisa em lista.
"""
def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)

L = [10, 20, 25, 30]
print('Indice de 25 =>', pesquise(L, 25))
print('Indice de 27 =>', pesquise(L, 27))

