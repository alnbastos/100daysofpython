# Exemplo de instrução de parada (BREAK)
soma = 0

while True:
    valor = int(input('Digite um número para somar ou 0 para sair: '))
    if valor == 0:
        break
    soma += valor
print(soma)
