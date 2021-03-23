"""
(23/03/2021) Escreva um programa que exiba uma lista de opções (menu): adição, subtração, divisão, multiplicação e sair.
Imprima a tabuada da operação escolhida. Repita até que a opção saída seja escolhida.
"""
while True:
    print('--- MENU ---')
    print('1 - Adição')
    print('2 - Subtração')
    print('3 - Divisão')
    print('4 - Multiplicação (Tabuada)')
    print('0 - Sair')
    opcao = int(input('Opção: '))

    if opcao == 0:
        break
    elif opcao >= 1 and opcao < 4:
        numero = int(input('Número: '))
        cont = 1
        while cont <= 10:
            if opcao == 1:
                print(f'{numero} + {cont} = {numero + cont}')
            elif opcao == 2:
                print(f'{numero} - {cont} = {numero - cont}')
            elif opcao == 3:
                print(f'{numero} / {cont} = {numero / cont}')
            elif opcao == 4:
                print(f'{numero} x {cont} = {numero * cont}')
            cont += 1
    else:
        print('\033[31mERROR! Insira os números das opções informadas.\033[m')

print('\nFIM DO PROGRAMA')
