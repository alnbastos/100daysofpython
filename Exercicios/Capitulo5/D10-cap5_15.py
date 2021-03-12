"""
(11/03/2021) Escreva um programa para controlar uma pequena máquina registradora. Você deve solicitar ao usuário que
digite o código do produto e a quantidade comprada. Utilize os código a seguir para obter o preço de cada produto:
Código 1 - Preço 0.50
Código 2 - Preço 1.00
Código 3 - Preço 4.00
Código 5 - Preço 7.00
Código 9 - Preço 8.00
Seu programa deve exibir o total das compras depois que o usuário digitar 0. Qualquer outro código deve gerar a mensagem
de erro "Código inválido".
"""
total_pagar = 0
while True:
    codigo = int(input('Número do código (0 para sair): '))
    preco = 0   # zera o valor de preço a cada repetição
    if codigo == 0:
        break
    elif codigo == 1:
        preco = 0.50
    elif codigo == 2:
        preco = 1
    elif codigo == 3:
        preco = 4
    elif codigo == 5:
        preco = 7
    elif codigo == 9:
        preco = 8
    else:
        print('\033[31mERRO! Código inválido.\033[m')
    if codigo == 1 or codigo == 2 or codigo == 3 or codigo == 5 or codigo == 9:
        quantidade = int(input('Quantidade a comprar: '))
        total_pagar = total_pagar + (preco * quantidade)

print(f'O total da sua compra é de R${total_pagar:.2f}')
