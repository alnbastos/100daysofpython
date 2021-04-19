# (16/04/2021) Simulacao de uma fila de banco
ultimo = 10
fila = list(range(1, ultimo + 1))

while True:
    print(f"\nExistem {len(fila)} clientes na fila.")
    print(f"Fila atual: {fila}")
    print("F - Adicionar cliente no fim da fila")
    print("A - Realizar atendimento")
    print("S - Sair")
    opcao = str(input("Opcao (F, A ou S): ")).lower()
    if opcao == "a":
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia. Ninguem para atender")
    elif opcao == "f":
        ultimo += 1
        fila.append(ultimo)
    elif opcao == "s":
        break
    else:
        print("Opcao invalida. Insira A, F ou S")