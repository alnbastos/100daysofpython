"""
(19/04/2021) Modifique o programa 6.9 de forma a realizar a mesma tafera, mas sem utilizar a variável achou.
"""
L = [15, 7, 27, 39]
p = int(input('Digite o valor a procurar: '))
x = 0

while x < len(L):
    if L[x] == p:
        break
    x += 1
if x < len(L):
    print(f'{p} achado na posição {x}')
else:
    print(f'{p} não encontrado')

