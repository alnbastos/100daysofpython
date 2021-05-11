#(11/05/2021) Exemplo 8.8 - Exemplo de validacao sem usar uma funcao

while True:
    v = int(input('Digite um valor entre 0 e 5: '))
    if v < 0 or v > 5:
        print('Valor invalido.')
    else:
        break

