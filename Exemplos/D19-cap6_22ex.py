# (23/04/2021) Exemplo de dicionário com estoque e operações de  venda
estoque = {
    'Tomate': [1000, 2.30],
    'Alface': [500, 0.50],
    'Batata': [2001, 1.20],
    'Feijão': [100, 1.50]
}
venda = [['Tomate', 5], ['Batata', 10], ['Alface', 5]]
total = 0

print('Vendas: \n')
for operacao in venda:
    produto, quantidade = operacao  # produto = operacao[0], quantidade = operacao[1]
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto:12s}: {quantidade:3d} x {preco} = {custo}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo total: {total}\n')

print('Estoque: \n')
for chave, dados in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço: {dados[1]}\n')
