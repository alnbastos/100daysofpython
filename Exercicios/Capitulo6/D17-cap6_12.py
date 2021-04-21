"""
(20/04/2021) Altere o exemplo 6.8 para imprimir o menor valor elemento da lista.
"""
L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
    if e < minimo:
        minimo = e
print(minimo)
