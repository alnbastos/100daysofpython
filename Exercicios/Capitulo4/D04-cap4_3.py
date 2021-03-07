"""
(23/02/2021) Escreva um programa que leia três números e que imprima o maior e o menor.
"""
print('MAIOR E MENOR VALOR')
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))

if a > b:
    print(f'O primeiro valor é maior! {a} é MAIOR que {b}')

if a == b:
    print('Os dois valores são iguais')

if b > a:
    print(f'O segundo valor é maior! {b} é MAIOR que {a}')
