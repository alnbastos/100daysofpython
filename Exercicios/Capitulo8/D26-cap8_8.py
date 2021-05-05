"""
(05/05/2021) Usando a função MDC definida no exercício anterior, defina uma função para calcular o menor múltiplo comum
(MMC) entre dois números.
"""
def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    return abs(a * b) / mdc(a, b)

print('MMC 10 e 5 => ', mmc(10, 5))
print('MMC 32 e 24 =>', mmc(32, 24))
print('MMC 5 e 3 =>  ', mmc(5, 3))
