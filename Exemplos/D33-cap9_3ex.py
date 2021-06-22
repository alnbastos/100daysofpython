# (22/06/2021) Gravacao de numeros pares e impares em arquivos diferentes
with open('Cap9_arquivos//impares_ex3.txt', 'w') as impares:
    with open('Cap9_arquivos//pares_ex3.txt', 'w') as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f'{n}\n')
            else:
                impares.write(f'{n}\n')

