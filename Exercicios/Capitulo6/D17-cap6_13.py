"""
(20/04/2021) A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista temp = [-10, -8, 0, 1, 2, 5, -2, -4].
Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
"""
# impriimir a menor, maior e a média da temperatura

temp = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = temp[0]
menor = temp[0]
soma = 0

for t in temp:
    soma += t
    if t > maior:
        maior = t
    else:
        menor = t

print(f'A MAIOR temperatura é: {maior} °C')
print(f'A MENOR temperatura é: {menor} °C')
print(f'A MEDIA das temperaturas é: {soma / len(temp)} °C')
