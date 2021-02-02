# Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

def linha(msg=''):
    print('-'*30)
    print(msg)


linha('PRINT TUDO:')
nome = 'Geek University'
for indice, letra in enumerate(nome):
    print(indice, letra)

linha('PRINT SEM INDICE:')
for _, letra in enumerate(nome):
    print(letra, end='')
print()

linha('PRINT EMOJI EM ESCADA')
emoji = '\U0001F60D'
for num in range(1, 11):
    print(emoji * num)

