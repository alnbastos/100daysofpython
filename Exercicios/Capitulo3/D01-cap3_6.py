"""
(16/02/2021) Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado. Para ser aprovado,
todas as médias do aluno devem ser maiores que 7. Considere que o aluno cursa apenas três matérias, e que a nota de
cada uma está armazaenada nas seguintes variáveis: matéria1, matéria2 e matéria3.
"""
nome_aluno = str(input('Digite o nome: ')).title()
media1 = int(input('Insira a média da 1º matéria: '))
media2 = int(input('Insira a média da 2º matéria: '))
media3 = int(input('Insira a média da 3º matéria: '))

print(f'O(a) aluno(a) {nome_aluno} passou?', end=' ')

if media1 > 7 and media2 > 7 and media3 > 7:
    print('\033[32mSim\033[m')
else:
    print('\033[31mNão\033[m')

#  if media1 > 7 (true ou false) and media2 > 7 (true ou false) and media3 > 7:
# verifica cada nota (operador relacional) antes de executar o operador lógico.
