"""
(19/04/2021) Faça um programa que leia uma expressão com parenteses. Usando pilhas, verifique se os parenteses foram
abertos e fechados na ordem correta.
"""
expressao = input('Expressão: ')
x = 0
pilha = []
while x < len(expressao):
    if expressao[x] == '(':
        pilha.append('(')
    if expressao[x] == ')':
        if len(pilha) > 0:
            topo = pilha.pop(-1)
        else:
            pilha.append(')')  # Força a mensagem de erro
            break
    x = x + 1
if len(pilha) == 0:
    print('OK')
else:
    print('Erro')
