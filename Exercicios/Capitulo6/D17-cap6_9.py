"""
(20/04/2021) Modifique o exemplo 6.6 para pesquisar dois valores. Em vez de apenas p, leia outro valor v que também
será procurado. Na impressão, indique qual dos dois valores foi achado primeiro.
"""
L = [15, 7, 27, 39]
p = int(input('Primeiro valor a pesquisar: '))
v = int(input('Segundo valor a pesquisar: '))
x = 0
achouV = False
achouP = False
primeiro = 0

while x < len(L):
    if L[x] == p:
        achouP = True
        if not achouV:
            primeiro = 1
    if L[x] == v:
        achouV = True
        if not achouP:
            primeiro = 2
    x += 1

if achouP:
    print(f'{p} encontrado')
else:
    print(f'{p} não encontrado')

if achouV:
    print(f'{v} encontrado')
else:
    print(f'{v} não encontrado')
    
if primeiro == 1:
    print("p foi achado antes de v")
elif primeiro == 2:
    print("v foi achado antes de p")