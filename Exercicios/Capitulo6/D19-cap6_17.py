"""
(23/04/2021) Altere o programa 6.22 de forma a solicitar ao usuário o produto e a quantidade vendida. Verifique se o nome
do produto digitado existe no dicionário, e só então efetue a baixa em estoque.
"""
estoque = {
    'Tomate': [1000, 2.30],
    'Alface': [500, 0.50],
    'Batata': [2001, 1.20],
    'Feijão': [100, 1.50]
}
total = 0
venda = []

while True:
    venda_produto = str(input('Insira o nome do produto desejado (Sair p/ sair): ')).title()
    if venda_produto == 'Sair':
        break
    if venda_produto in estoque:
        venda_quant = int(input(f'Insira a quantidade de {venda_produto}({estoque[venda_produto][0]}): '))
        if venda_quant <= estoque[venda_produto][0]:
            preco = estoque[venda_produto][1]
            custo = preco * venda_quant
            print(f'{venda_produto:12s}: {venda_quant:3d} x {preco} = {custo}')
            estoque[venda_produto][0] -= venda_quant
            total += custo
        else:
            print('Quantidade solicitada não disponível.')
        print()
    else:
        print('Este produto não está no estoque.\n')
    
print(f'Custo total: {total}\n')

print('Estoque: \n')
for chave, dados in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço:  {dados[1]}\n')
