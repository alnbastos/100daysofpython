"""
(02/03/2021) Altere o exemplo de programa anterior para exibir os resultados no mesmo formato
de uma tabuada: 2x1 = 2, 2x2 = 4...
"""
print('--- TABUADA ---')
num = int(input('Tabuada de: '))
x = 0

while x <= 9:
    x += 1
    mult = num * x
    print(f'{num} x {x} = {mult}')
