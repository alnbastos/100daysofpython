# (07/06/2021) Navegando listas a partir do tipo de seus elementos
L = ['a', ['b', 'c', 'd'], 'e']
for x in L:
    if type(x) is str:
        print('String:', x)
    else:
        print('Lista:', end='')
        for z in x:
            print(f' {z}', end='')
        print()

