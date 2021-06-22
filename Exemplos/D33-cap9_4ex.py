# (21/06/2021) With em uma so linha
with open('Cap9_arquivos//impares_ex3.txt', 'w') as impares, open('Cap9_arquivos//pares_ex3.txt', 'w') as pares:
    for n in range(0, 100):
        if n % 2 == 0:
            pares.write(f'{n}\n')
        else:
            impares.write(f'{n}\n')

