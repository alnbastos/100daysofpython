"""
(28/04/2021) Modifique o Exemplo 7.2 para utilizar listas de strings para desenhar o boneco da forca. Você pode utilizar
uma lista para cada linha e organizá-las em uma lista de listas. Em vez de controlar quando imprimir cada parte, desenhe
nessa listas, substituindo o elemento a desenhar.
"""
palavras = [
          'casa',
          'bola',
          'mangueira',
          'uva',
          'garrafa',
          'computador',
          'cachorro',
          'caderno',
          'arroz'
     ]

indice = int(input('Digite um numero: '))
palavra = palavras[(indice * 776) % len(palavras)]
for x in range(100):
    print()

erros = 0
digitadas = []
acertos = []
linhas = []
linhas_txt = """
X==:==
X  :
X  
X  
X  
X  
=======

"""

for linha in linhas_txt.splitlines():
    linhas.append(list(linha))

while True:
    senha = ''
    for letra in palavra:
        senha += letra if letra in acertos else '.'
    print(senha)
    if senha == palavra:
        print('Você acertou!')
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
            if erros == 1:
                linhas[3].append('O')
            elif erros == 2:
                linhas[4].append('|')
            elif erros == 3:
                linhas[4][2] = '/'  # braço esquerdo
            elif erros == 4:
               linhas[4].append("\\")   # braço direito
            elif erros == 5:
                linhas[5][2] = '/'  # perna esquerda
            elif erros == 6:
                linhas[5].append(' ')
                linhas[5].append('\\')   # perna direita
        
        for l in linhas:
            print(''.join(l))
        if erros == 6:
            print('Enforcado!')
            print('A palavra secreta era:', palavra)
            break
