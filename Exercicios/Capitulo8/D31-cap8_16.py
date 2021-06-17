"""
(16/06/2021) Escreva um generator capaz de gerar a série de números primos.
"""


def num_primos(n):
    cont = 1
    yield 2  # 2 é o único primo que é par
    divisor = 3
    dividendo = 3
    while cont < n:
        if dividendo % divisor == 0:
            if dividendo == divisor:  # Se dividendo é igual a dividor, todos os valores divisor já foram testados
                yield dividendo  # dividendo é primo
                cont += 1  # contador
            dividendo += 2  # Passa para o próximo número ímpar
            divisor = 3  # Recomeça a dividir por 3
        elif divisor < dividendo:  # Continua tentando?
            divisor += 2  # Incrementa o divisor para o próximo ímpar
        else:
            dividendo += 2  # Tenta outro número ímpar


for primos in num_primos(10):
    print(primos)
