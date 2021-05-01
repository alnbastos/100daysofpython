"""
(30/04/2021) Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
Valores esperados:
multiplo(8, 4) == True
"""


def multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False


print('multiplo(8, 4) =>', multiplo(8, 4))
print('multiplo(7, 3) =>', multiplo(7, 3))
print('multiplo(5, 5) =>', multiplo(5, 5))
