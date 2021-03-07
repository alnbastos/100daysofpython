"""
(16/02/2021) Conferir o resultado das expressões.
"""
a = int(input('Valor de A: '))
b = int(input('Valor de B: '))

c = str(input('Valor lógico de C: ')).lower()
if c == 'false':
    c = False
elif c == 'true':
    c = True

d = str(input('Valor lógico de D: ')).lower()
if d == 'false':
    d = False
elif d == 'true':
    d = True

x = a > b and c or d

print(f'Resultado da expressão: {x}')
