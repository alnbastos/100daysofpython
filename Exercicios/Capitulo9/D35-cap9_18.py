"""
(13/07/2021) Altere o Programa 9.6 para exibir o tamanho da agenda no menu principal.
"""
# (28/06/2021) Controle de uma agenda de telefones
agenda = []


def pede_nome():
    return input('Nome: ')


def pede_telefone():
    return input('Telefone: ')


def mostra_dados(nome, telefone):
    print(f'Nome: {nome} | Telefone: {telefone}')


def pede_nome_arquivo():
    return input('Nome do arquivo: ')


def pesquisa(nome):
    mnome = nome.lower()
    for p, e in enumerate(agenda):
        if e[0].lower() == mnome:  # e[0] pega a primeira letra do elemento de agenda.
            return p    # p é o indice
    return None


def novo():
    global agenda
    nome = pede_nome()
    telefone = pede_telefone()
    agenda.append([nome, telefone])


def apaga():
    global agenda
    nome = pede_nome()  # recebe o nome, pela função pede_nome() que possui input
    p = pesquisa(nome)  # joga o nome dentro de pesquisa()
    if p is not None:
        del agenda[p]   # apaga dentro de agenda, pela indice retornado em pesquisa()
    else:
        print('Nome não encontrado')    # caso a função pesquisa() retornar None


def altera():
    p = pesquisa(pede_nome())   # indice de agenda()
    if p is not None:
        nome = agenda[p][0]
        telefone = agenda[p][1]
        print('Enontrado:')
        mostra_dados(nome, telefone)
        nome = pede_nome()
        telefone = pede_telefone()
        agenda[p] = [nome, telefone]
    else:
        print('Nome não encontrado')


def lista():
    print('\nAgenda\n\n------')
    for e in agenda:
        mostra_dados(e[0], e[1])
    print('------\n')


def le():
    global agenda
    nome_arquivo = pede_nome_arquivo()
    try:
        with open(f'arquivos//{nome_arquivo}', 'r', encoding='utf-8') as arquivo:
            agenda = []
            for l in arquivo.readlines():
                nome, telefone = l.strip().split('#')
                agenda.append([nome, telefone])
    except FileNotFoundError:
        print('\nArquivo não encontrado')


def grava():
    nome_arquivo = pede_nome_arquivo()
    with open(f'arquivos//{nome_arquivo}', 'w', encoding='utf-8') as arquivo:
        for e in agenda:
            arquivo.write(f'{e[0]}#{e[1]}\n')


def tamanho():
    nome_arquivo = pede_nome_arquivo()
    arquivo = open(nome_arquivo)
    print(len(arquivo))
    arquivo.close()


def valida_faixa_inteiro(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return valor
        except ValueError:
            print(f'Valor inválido, favor digitar entre {inicio} e {fim}')


def menu():
    print(f"""
    1 - Novo
    2 - Altera
    3 - Apaga
    4 - Lista
    5 - Grava
    6 - Lê

    0 - Sair
    
    Agenda: {len(agenda)} contato(s)
    """)
    return valida_faixa_inteiro('Escolha uma opção: ', 0, 6)


while True:
    opcao = menu()
    if opcao == 0:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        altera()
    elif opcao == 3:
        apaga()
    elif opcao == 4:
        lista()
    elif opcao == 5:
        grava()
    elif opcao == 6:
        le()
    elif opcao == 7:
        tamanho()
