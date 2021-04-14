"""
(13/04/2021) Modifique o Programa de exemplo 6.1 para ler 7 notas em vez de 5.
"""
notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
cont = 0

while cont < 3:
    notas[cont] = float(input(f'Nota {cont}: '))
    soma += notas[cont]
    cont += 1

print(f'Média: {soma/cont:.2f}')
