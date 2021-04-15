"""
(14/04/2021) Faça um programa que percorra duas listas e gere uma terceira sem elementos repetidos.
"""
list_a = []
list_b = []
list_c = []
cont = 0

while True:
    num = str(input('Insira os números da Lista A (s para sair): ')).lower()
    if num == 's':
        break
    list_a.append(int(num))

while True:
    num = str(input('Insira os números da Lista B (s para sair): ')).lower()
    if num == 's':
        break
    list_b.append(int(num))

duas_listas = list_a[:]  # copia da lista_a
duas_listas.extend(list_b)

x = 0
while x < len(duas_listas):
    y = 0
    while y < len(list_c):
        if duas_listas[x] == list_c[y]:
            break
        y = y + 1
    if y == len(list_c):
        list_c.append(duas_listas[x])
    x = x + 1

x = 0
while x < len(list_c):
    print(f"{x}: {list_c[x]}")
    x = x + 1
