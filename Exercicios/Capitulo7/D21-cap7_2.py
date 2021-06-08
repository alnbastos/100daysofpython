"""
(27/04/2021) Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
1 string: AAACTBF
2 string: CBT
Resultado: CBT
A ordem dos caracteres da string gerada não é importante, mas deve conter todas as letras comuns a ambas.
"""
primeira = str(input('Primeira string: '))
segunda = str(input('Segunda string: '))
terceira = '' #para evitar repetição

for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra

if terceira == '':
    print('Caracteres não encontrados')
else:
    print('Caracteres comuns:', terceira)