# Apresentação de números
num = [0, 0, 0, 0, 0]
cont = 0

while cont < 5:
    num[cont] = float(input(f'Número {cont + 1}: '))
    cont += 1
while True:
    opcao = int(input('Qual opção deseja imprimir (0 p/ sair): '))
    if opcao == 0:
        break
    print(f'Você escolheu o número: {num[opcao - 1]}')
