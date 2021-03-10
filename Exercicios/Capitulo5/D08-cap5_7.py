"""
(02/03/2021) Modifique o programa anterior de forma que o usuário também digite o inicio e o fim da tabuada, em
de começar com 1 e 10.
"""
print('--- TABUADA: NUMERO X INICIO-FIM ---')
num = int(input('Tabuada de: '))
inicio = int(input('Digite o inicío da tabuada: '))
fim = int(input('Digite o fim da tabuada: '))

if inicio >= fim:
    print('ERRO! O valor do início não pode ser maior ou igual ao fim.')
else:
    while inicio <= fim:
        mult = num * inicio
        print(f'{num} x {inicio} = {mult}')
        inicio += 1
