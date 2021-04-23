"""
(22/04/2021) O que acontece quando a lista já está ordenada? Rastreie o Exemplo 6.20, mas com a lista L = [1, 2, 3, 4, 5].
R : Por já esta ordenado, o programa irá verificar se L[x] > L[x+1] é verdadeiro a cada verificação de x < (fim - 1), mas não
realizando a troca, já que nenhum elemento é maior que próximo.
"""
L = [1, 2, 3, 4, 5]
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