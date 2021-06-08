"""
(27/04/2021) Escreva um programa que leia duas strings e gere uma terceira, na qual os caracteres da segunda foram retirados
da primeira.
1 String: AATTGGAA
2 String: TG
3 String: AAAA
"""
primeira = str(input('Primeira string: ')).upper()
segunda = str(input('Segunda string: ')).upper()
terceira = ''

for letra in primeira:
    if letra not in segunda:
        terceira += letra

if terceira == '':
    print('Todos os caracteres foram removidos')
else:
    print(f'Os caracteres {segunda} foram removidos de {primeira}, gerando: {terceira}')
