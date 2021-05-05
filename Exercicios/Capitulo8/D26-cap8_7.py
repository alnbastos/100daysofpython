"""
(05/05/2021) Defina uma função recursiva que calcule o maior divisor comum (MDC) entre dois números, a e b, em que a > b.
"""
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

print('MDC de 1 e 2 => ', mdc(1, 2))
print('MDC de 10 e 5 =>', mdc(10, 5))
print('MDC de 7 e 13 =>', mdc(7, 13))
