# (11/05/2021) - Funcao soma com parametros obrigatorios e opcionais
def soma(a, b, imprime=True):
    s = a + b
    if imprime:
        print(s)
    return s

soma(1, 3)
soma(5, 3, True)

