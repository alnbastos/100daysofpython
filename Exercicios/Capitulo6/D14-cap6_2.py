"""
(14/04/2021) Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
"""
list_a = []
list_b = []
list_c = []

while True:
    print('1 - Lista A \n2 - Lista B\n0 - Sair')
    opcao = int(input('Deseja adicionar números em qual lista? '))
    if opcao == 1:
        while True:
            num = str(input('LISTA A - Número (s para sair): ')).lower()
            if num == 's':
                break
            else:
                list_a.append(int(num))
    elif opcao == 2:
        while True:
            num = str(input('LISTA B - Número (s para sair): ')).lower()
            if num == 's':
                break
            else:
                list_b.append(int(num))
    elif opcao == 0:
        break
    else:
        print('ERROR! Insira opções válidas.')

list_c += list_a
list_c += list_b
print(f'A terceira lista é a junção da lista A e B. \nTendo o resultado: {list_c}')
