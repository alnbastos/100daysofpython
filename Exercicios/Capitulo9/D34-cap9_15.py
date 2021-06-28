"""
(28/06/2021) Altere o programa 7.2, o jogo da forca. Utilize um arquivo em que uma palavra seja gravada a cada linha. Use o editor de textos para gerar o arquivo. Ao iniciar o programa, utilize esse arquivo para carregar (ler) a lista de palavras. Experimente tambem perguntar o nome do jogador e gerar um arquivo com o numero de acertos dos cinco melhores.
"""
import sys
import random

palavras = []
placar = {}

def carrega_palavras():
    with open('arquivos//palavras_ex15.txt', 'r', encoding='utf-8') as arquivo:
        for palavra in arquivo.readlines():
            palavra = palavra.strip().lower()
            if palavra != '':
                palavras.append(palavra)

def carrega_placar():
    with open('arquivos//placar_ex15.txt', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo.readlines():
            linha = linha.strip()
            if linha != '':
                usuario, contador = linha.split(';')
                placar[usuario] = int(contador)

def salva_placar():
    with open('arquivos//placar_ex15.txt', 'w', encoding='utf-8') as arquivo:
        for usuario in placar.keys():
            arquivo.write(f'{usuario};{placar[usuario]}\n')

def atualize_placar(nome):
    if nome in placar:
        placar[nome] += 1
    else:
        placar[nome] = 1
    salva_placar()

def exibe_placar():
    placar_ordenado = []
    for usuario, score in placar.items():
        placar_ordenado.append([usuario, score])
    placar_ordenado.sort(key=lambda score: score[1])
    print('\nMelhores jogadores por numero de acertos:\n')
    placar_ordenado.reverse()
    for up in placar_ordenado:
        print(f'{up[0]:30s} {up[1]:10d}')

carrega_palavras()
carrega_placar()

palavra = palavras[random.randint(0, len(palavras)-1)]

digitadas = []
acertos = []
erros = 0

while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Você acertou!')
        nome = str(input('Digite seu nome: '))
        atualize_placar(nome)
        break
    tentativa = input('\nDigite uma letra: ').lower().strip()
    if tentativa in digitadas:
        print('Você já tentou esta letra!')
        continue
    else:
        digitadas += tentativa
        if tentativa in palavra:
            acertos += tentativa
        else:
            erros += 1
            print('Você errou!')

        print('X==:==\nX  : ')
        print('X  O ' if erros >= 1 else 'X')
        
        linha2 = ''
        if erros == 2:
            linha2 = '  | '
        elif erros == 3:
            linha2 = ' \| '
        elif erros >= 4:
            linha2 = ' \|/'
        print(f'X{linha2}')
        
        linha3 = ''
        if erros == 5:
            linha3 += ' /  '
        elif erros >= 6:
            linha3 += ' / \ '
        print(f'X{linha3}')
        print('X\n===========')
        if erros == 6:
            print('Enforcado!')
            break

exibe_placar()

