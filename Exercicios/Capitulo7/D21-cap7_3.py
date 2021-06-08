"""
(27/04/2021) Escreva um programa que leia duas strings e gere uma terceira apenas com os caracteres que aparecem
em uma delas.
1 string: CTA
2 string: ABC
Resultado: BT
A ordem dos caracteres da string gerada não é importante.
"""
primeira = str(input('Primeira string: '))
segunda = str(input('Segunda string: '))
terceira = '' 

for letra in primeira:
    if letra in segunda and letra not in terceira:
        terceira += letra

for letra in segunda:
    # not in terceira, para evitar repetição
    if letra in primeira and letra not in terceira:
        terceira += letra

if terceira == '':
    print('Caracteres não encontrados')
else:
    print('Caracteres incomuns:', terceira)