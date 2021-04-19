"""
(16/04/2021) crie um programa que possa trabalhar com varios comandos digiados de uma so vez.
Faca de forma a considerar operacao como string. 
"""
ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("F - Adicionar cliente no fim da fila")
    print("A - Realizar atendimento")
    print("S - Sair")
    opcao = str(input("Opcao (F, A ou S): ")).lower()
    x = 0
    sair = False

    while x < len(opcao):
        if opcao[x] == "a":
            if len(fila) > 0:
                atendido = fila.pop(0)
                print(f"Cliente {atendido} atendido")
            else:
                print("Fila vazia. Ninguem para atender")
        elif opcao[x] == "f":
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