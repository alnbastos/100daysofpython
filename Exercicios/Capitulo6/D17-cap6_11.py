"""
(20/04/2021) Modifique o programa 6.6 usando for. Explique porque nem todos os while podem ser transformados em for.
Explicação: o primeiro While (True) não pode ser convertido em for pois o número de repetição é desconhecido no inicio.
"""
ultimo = 0
fila1 = []
fila2 = []

while True:
    print(f'\nExistem {len(fila1)} clientes na fila 1.')
    print(f'Existem {len(fila2)} clientes na fila 2.')
    print(f'Fila 1 atual: {fila1}')
    print(f'Fila 2 atual: {fila2}')
    print('Fila 1:  A - Realizar atendimento  |  F - Adicionar cliente')
    print('Fila 2:  B - Realizar atendimento  |  G - Adicionar cliente')
    print('S - Sair')
    opcao = str(input('Opção (A, B, F, G ou S): ')).lower()
    x = 0
    sair = False
    for op in opcao:
        if op == 'a' or op == 'f':
            fila = fila1
        else:
            fila = fila2 
        if op == 'a' or op == 'b':
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia! Ninguém para atender.")
        elif op == 'f' or op == 'g':
            ultimo += 1
            fila.append(ultimo)
        elif op == 's':
            sair = True
            break
        else:
            print(f"Operação inválida: {op} na posição {x}! Digite apenas F, A ou S!")
        x += 1 
    if sair:
        break
