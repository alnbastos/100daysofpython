"""
(30/04/2021) Escreva uma função que retorne o maior de dois números.
Valores esperados:
maximo(5, 6) == 6
"""


def maior(a, b):
    if a > b:
        return a
    else:
        return b


print('maior(5, 6) =>', maior(5, 6))
print('maior(2, 1) =>', maior(2, 1))
print('maior(7, 7) =>', maior(7, 7))
