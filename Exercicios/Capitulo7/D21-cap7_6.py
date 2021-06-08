"""
(27/04/2021) Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres
da segunda pelos da terceira.
1 String: AATTCGAA
2 String: TG
3 String: AC
Resultado: AAAACCAA
"""
primeira = input('Primeira string: ')
segunda = input('Segunda string: ')
terceira = input('Terceira string: ')

if len(segunda) == len(terceira):
    resultado = ''
    for letra in primeira:
        posição = segunda.find(letra)
        if posição != -1:
            resultado += terceira[posição]
        else:
            resultado += letra

    if resultado == '':
        print('Todos os caracteres foram removidos.')
    else:
        print(f'Os caracteres {segunda} foram substituidos por '
              f'{terceira} em {primeira}, gerando: {resultado}')
else:
    print('ERRO: A segunda e a terceira string devem ter o mesmo tamanho.')