"""
Tuplas.
1 - São representadas por parênteses ();
2 - não IMUTÁVEIS. Toda operação em uma tupla, gera uma nova tupla.

Deve utilizar tuplas SEMPRE que NÃO precisar modificar os dados contidos em uma coleção (ex.: tupla com meses do ano)

Por quê utilizar tuplas?
1 - são mais rápidas do que listas;
2 - deixam seu código mais seguro, isso porque trabalhar com elementos imutáveis traz segurança para o código.

"""
'''# CUIDADO 1: as tuplas são representados por (), mas veja:
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))

tupla = tuple(range(10))
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))'''

times = ('Corithians', 'São Paulo', 'Palmeiras', 'Flamengo')

print(f'Os times são: {times}')
print(f'Os 2 primeiros: {times[:2]}')
print(f'Os 2 últimos: {times[-2:]}')
print(f'Times em ordem alfábetica: {sorted(times)}')
print(f'O times Palmeiras está na {times.index("Palmeiras")} posição')