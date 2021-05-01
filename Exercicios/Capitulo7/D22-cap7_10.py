# (29/04/2021) Jogo da velha
tabuleiro = [
    [7, 8, 9],  # linha 1
    [4, 5, 6],  # linha 2
    [1, 2, 3]  # linha 3
]

ganhou = [
    [7, 8, 9],  # linha 1
    [4, 5, 6],  # linha 2
    [1, 2, 3],  # linha 3

    [7, 4, 1],  # coluna 1
    [8, 5, 2],  # coluna 2
    [9, 6, 3],  # coluna 3

    [1, 5, 9],  # diagonais
    [3, 5, 7]
]

jogadas = 1
jogando = True
jogador = 'X'


while True:
    posicao = int(input('posição: '))

    if jogadas == 9:
        print('Deu velha! Ninguém ganhou.')
        break
    if not jogando:
        break
    if posicao < 1 or posicao > 9:
        print('Opção inválida.')
    else:
        if posicao in tabuleiro[0]:  # verificar a posição na linha 1
            posicao_tab = tabuleiro[0].index(posicao)  # pegar o indice da posicao digitada
            tabuleiro[0][posicao_tab] = jogador  # atualizar o número pelo jogador (X ou O1)

        elif posicao in tabuleiro[1]:  # verificar a posição na linha 2
            posicao_tab = tabuleiro[1].index(posicao)
            tabuleiro[1][posicao_tab] = jogador

        elif posicao in tabuleiro[2]:  # verificar a posição na linha 3
            posicao_tab = tabuleiro[2].index(posicao)
            tabuleiro[2][posicao_tab] = jogador
        else:
            print('repetido')
            continue
        jogador = "X" if jogador == "O" else "O"  # Alterna jogador
        jogadas += 1

    for g in ganhou:
        for x in g:
            if tabuleiro[posicao[x][0]][posicao[x][1]] != jogador:
                break
            else:  # Se o for terminar sem break, todas as posicoes de p pertencem ao mesmo jogador
                print(f"O jogador {jogador} ganhou ({g}): ")
                jogando = False
                break

    for linha in tabuleiro:
        print(linha)
