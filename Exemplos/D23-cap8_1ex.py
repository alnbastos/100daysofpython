# (30/04/2021) Pesquisa em uma lista

def pesquise(lista, valor):
    for indice, elemento in enumerate(L):
        if elemento == valor:
            return indice
    return None


L = [10, 20, 25, 30]
print('Indice de 25 =>', pesquise(L, 25))
print('Indice de 27 =>', pesquise(L, 27))
