"""
(16/06/2021) Escreva um generator capaz de gerar a série de Fibonacci.
"""
def fibonacci(n):
    p = 0
    s = 1
    while n > 0:
        yield s
        p, s = s, s + p
        n -= 1


for generator in fibonacci(10):
    print(generator, end=' ')
