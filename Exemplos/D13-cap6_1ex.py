# Cálculo de média
notas = [0, 0, 0, 0, 0]
soma = 0
cont = 0

while cont < 5:
    notas[cont] = float(input(f'Nota {cont}: '))
    soma += notas[cont]
    cont += 1

cont = 0
while cont < 5:
    print(f'Nota {cont}: {notas[cont]:6.2f}')
    cont += 1

print(f'Média: {soma/cont:5.2f}')
