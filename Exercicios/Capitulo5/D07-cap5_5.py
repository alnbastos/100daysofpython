"""
(27/02/2021) Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.
"""
fim = int(input('Digite o último número a imprimir: '))
cont = 1
x = 3
while cont <= fim:
    print(x)
    x += 3
    cont += 1
