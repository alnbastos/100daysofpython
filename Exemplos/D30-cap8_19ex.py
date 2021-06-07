# (07/06/2021) - Modulo soma que importa entrada (D30-cap8_18ex.py)
import D30cap8_18ex

L = []
for x in range(10):
    L.append(D30cap8_18ex.valida_inteiro('Digite um numero: ', 0, 20))
print('Soma:', sum(L))

