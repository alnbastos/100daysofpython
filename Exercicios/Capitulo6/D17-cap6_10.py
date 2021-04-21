"""
(20/04/2021) Modifique o exemplo 6.6 de forma a pesquisar p e v em toda a lista e informando o usuário a posição onde p
e a posição onde v foram encontrados.
"""
L = [15, 7, 27, 39]
p = int(input('Primeiro valor a pesquisar: '))
v = int(input('Segundo valor a pesquisar: '))
x = 0
achouV = False
achouP = False
posicaoP = 0
posicaoV = 0
primeiro = 0

while x < len(L):
    if L[x] == p:
        achouP = True
        posicaoP = x
        if not achouV:
            primeiro = 1
    if L[x] == v:
        achouV = True
        posicaoV = x
        if not achouP:
            primeiro = 2
    x += 1

if achouP:
    print(f'P: {p} encontrado na posição {posicaoP}')
else:
    print(f'P: {p} não encontrado')

if achouV:
    print(f'V: {v} encontrado na posição {posicaoV}')
else:
    print(f'V: {v} não encontrado')
    
if primeiro == 1:
    print("P foi encontrado antes de V")
elif primeiro == 2:
    print("V foi encontrado antes de P")