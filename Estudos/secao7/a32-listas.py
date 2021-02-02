def texto(msg):
    print('-' * 30)
    print(f'\033[32m {msg:^27} \033[m')
    print('-' * 30)


lista1 = list(range(11))

if 4 in lista1:
    print('Encontrei o numero 4.')
else:
    print('Nao encontrei o numero 4.')

lista2 = [1, 2, 5, 3, 7, 54, 23, 11, 57, 7, 332, 9]

# ordena a lista
texto('Ordena lista')
lista2.sort()
print(lista2)

# adiciona um valor ou conjunto, no final da lista.
texto('Adicionar valor')
lista2.append([8, 3, 1])
print(lista2)

# inserir um conjunto de elementos, porem adiciona valores um por um. NAO aceita valor unico, funçao do append.
# no final da lista.
texto('Inserir conjunto')
lista2.extend([123, 44, 67])
print(lista2)

# inserir elemento com indice especificado
texto('Inserir elemento')
lista2.insert(2, 'Novo valor')
print(lista2)

# juntar duas listas
texto('Juntar duas listas')
lista3 = lista1 + lista2
# ou
lista1.extend(lista2)
print(lista1)
print(lista3)

# inverter listas
texto('Inverter listas')
# forma1
lista1.reverse()
print(lista1)
# forma2
print(lista1[::-1])

# copiar lista
texto('Copiar lista')
lista4 = lista1.copy()
print(lista4)

# remover o ultimo elemento de uma lista
texto('Remover último elemento de uma lista (POP())')
lista1.pop()
print(lista1)

# remover um elemento pelo indice
texto('Remover um elemento pelo indice (POP(indice))')
lista1.pop(3)
print(lista1)

# convertendo string em lista
texto('Convertendo string em lista')
curso = 'Programação Python: Essencial'
curso1 = 'Programação,para,internet'
curso = curso.split()
curso1 = curso1.split(',')
print(curso, curso1)

# convertendo lista para string
texto('Convertendo lista para string')
curso_string = ' '.join(curso)
print(curso_string)

#Iterando sobre listas
# exemplo1 - FOR
texto('Iterando sobre listas - FOR INT ')
lista6 = list(range(11))
soma = 0
for elemento in lista6:
    print(elemento)
    soma += elemento
print(f'Valor da soma: {soma}')

# exemplo2 - FOR
texto('Iterando sobre listas - FOR STRING')
lista5 = list('Aline Magalhães Bastos')
soma = ' '
for elemento in lista5:
    print(elemento)
    soma += elemento
print(soma)

# exemplo1 - WHILE
texto('Iterando sobre listas - WHILE')
carrinho = []
produto = ' '
while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair do programa:")
    produto = input('Produto: ')
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Video 1:47:00