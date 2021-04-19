"""
(16/04/2021) Modifique o programa para trabalhar com duas filas. Considere A para atendimento
da fila 1; B para atendimento da fila 2. O mesmo para a chegada de clientes: F para fila 1; e 
G para a fila 2.
"""
ultimo = 0
fila1 = []
fila2 = []

while True:
    print(f"\nExistem {len(fila1)} clientes na fila 1. E {len(fila2)} na fila 2")
    print(f"Fila 1 atual: {fila1}")
    print(f"Fila 2 atual: {fila2}")
    print("Fila 1:  A - Realizar atendimento  |  F - Adicionar cliente no fim da fila")
    print("Fila 2:  B - Realizar atendimento  |  G - Adicionar cliente no fim da fila")
    print("S - Sair")
    opcao = str(input("Opcao (A, B, F, G ou S): ")).lower()
    x = 0
    sair = False

    while x < len(opcao):
        if opcao[x] == "a" or opcao[x] == "f":
            fila = fila1
        else:
            fila = fila2
        if opcao[x] == "a" or opcao[x] == "b":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia. Ninguem para atender")
        elif opcao[x] == "f" or opcao[x] == "g":
            ultimo += 1
            fila.append(ultimo)
        elif opcao[x] == "s":
            sair = True
            break
        else:
            print("Opcao invalida. Insira A, F ou S")
        x += 1
    if sair:
        break
