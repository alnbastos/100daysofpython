# (19/04/2021) pilha de pratos
prato = 5
pilha = list(range(1, prato + 1))

while True:
    print(f"\nExistem {len(pilha)} pratos na pilha.")
    print(f"Pilha atual: {pilha}")
    print("E - Empilhar um novo prato")
    print("D - Desempilhar")
    print("S - Sair")
    opcao = str(input("Opcao (E, D ou S): ")).lower()
    if opcao == "d":
        if len(pilha) > 0:
            lavado = pilha.pop(0)
            print(f"Prato {lavado} lavado")
        else:
            print("Pilha vazia. Nada para lavar.")
    elif opcao == "e":
        prato += 1
        pilha.append(prato)
    elif opcao == "s":
        break
    else:
        print("Opcao invalida. Insira E, D ou S.")
