"""
(11/03/2021) Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o
usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados,
assim como a soma e a média aritmética.
"""
soma = 0
cont = 0

while True:
    valor = int(input('Digite um número para somar ou 0 para sair: '))
    if valor == 0:
        break
    soma += valor
    cont += 1

print()
print(f'Números digitados: {cont}')
print(f'A soma dos números digitados é: {soma}')
print(f'A média aritmética dos números digitados é: {soma / cont}')
