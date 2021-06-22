"""
(22/06/2021) Crie um programa que leia os arquivos pares.txt e impares.txt e que crie um so arquivo paresimpares.txt com todas as linhas dos outros
dois arquivos, de forma a preservar a ordem numerica.
"""
def le_numero(arquivo):
    while True:
        numero = arquivo.readline()
        if numero == '':
            return None
        if numero.strip() != '':
            return int(numero)

def escreve_numero(arquivo, numero):
    arquivo.write(f'{numero}\n')

pares = open('arquivos//pares_ex3.txt', 'r')
impares = open('arquivos//impares_ex3.txt', 'r')
par_impar = open('arquivos//par_impar_ex3.txt', 'w')
num_par = le_numero(pares)
num_impar = le_numero(impares)

while True:
    if num_par is None and num_impar is None: # termina se ambos forem None
        break
    if num_par is not None and (num_impar is None or num_par <= num_impar):
        escreve_numero(arquivo=par_impar, numero=num_par)
        num_par = le_numero(pares)
    if num_impar is not None and (num_par is None or num_impar <= num_par):
        escreve_numero(arquivo=par_impar, numero=num_impar)
        num_impar = le_numero(impares)

par_impar.close()
pares.close()
impares.close()

