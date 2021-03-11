# Exemplo de acumulador x contador: Média aritmética
x = 1
soma = 0

while x <= 5:
    n = int(input(f'{x} Digite o número: '))
    soma = soma + n     # acumulador de n
    x += 1  # contador
print(f'Média: {soma / 5 :5.2f}')
