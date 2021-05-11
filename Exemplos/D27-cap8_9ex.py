#(11/05/2021) Exemplo 8.9 - Validacao de inteiro usando funcao

def faixa_int(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f'Valor invalido. Digite um valor entre {minimo} e {maximo}.')
        else:
            break

faixa_int('Digite um valor: ', 0, 5)

