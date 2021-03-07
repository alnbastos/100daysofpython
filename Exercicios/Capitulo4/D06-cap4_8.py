"""
(25/02/2021) Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar.
Você deve poder calcular soma, subtração, multiplicação e divisão. Exiba o resultado da operação solicitada.
"""
print('CALCULADORA')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

print('Operações:\n'
      '[1] Soma\n'
      '[2] Substração\n'
      '[3] Multiplicação\n'
      '[4] Divisão')
opcao = int(input('Opção: '))

if opcao == 1:    # soma
    calc = a + b
    sinal = '+'
elif opcao == 2:    # subtração
    calc = a - b
    sinal = '-'
elif opcao == 3:    # multiplicação
    calc = a * b
    sinal = '*'
elif opcao == 4:    # divisão
    calc = a / b
    sinal = '/'
else:
    print('ERROR! Insira uma opção entre 1 a 4')

print(f'Resultado: {a} {sinal} {b} = {calc}')
