# Adição de elementos à lista
lista = []

while True:
    num = int(input('Digite um número (0 p/ sair): '))
    if num == 0:
        break
    lista.append(num)

cont = 0
while cont < len(lista):
    print(lista[cont])
    cont += 1
