"""
(22/04/2021) O que acontece quando dois valores são iguais? Rastreie o Exemplo 6.20, mas com a lista L = [3, 3, 1, 5, 4].
R : O programa irá executar e realizará a verificação, quando chegar na linha onde verifica se L[x] > L[x + 1] dará falso
já que ambos os números são iguais, assim, continuando o programa e incrementando o indice (x) e indo para a verificação
dos próximos números.
"""
L = [3, 3, 1, 5, 4]
fim = 5
while fim > 1:
    trocou = False
    x = 0
    while x < (fim - 1):
        if L[x] > L[x + 1]:
            trocou = True
            temp = L[x]
            L[x] = L[x + 1]
            L[x + 1] = temp
        x += 1
    if not trocou:
        break
    fim -= 1

for e in L:
    print(e)