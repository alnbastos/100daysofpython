"""
(24/02/2021) Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a quantidade
de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
Calcule o preço a pagar de acordo com a tabela a seguir.
R: <= 500kWh - 0.40, > 500 - 0.65
C: <= 1000 - 0.55, > 1000 - 0.60
I: <= 5000 - 0.55, > 5000 - 0.60
"""
print('FORNECIMENTO DE ENERGIA ELÉTRICA')
quant_kwh = float(input('Quantidade de kWh consumida: '))
tipo_instalacao = str(input('Tipo de instalação (residência, indústria ou comércio): ')).lower()
kwh = quant_kwh

if tipo_instalacao[0] == 'r':
    tipo = 'Residência'
    if quant_kwh <= 500:
        preco_pagar = kwh * 0.40
    else:
        preco_pagar = kwh * 0.60
elif tipo_instalacao[0] == 'i':
    tipo = 'Indústria'
    if quant_kwh <= 1000:
        preco_pagar = kwh * 0.55
    else:
        preco_pagar = kwh * 0.60
elif tipo_instalacao[0] == 'c':
    tipo = 'Comércio'
    if quant_kwh <= 5000:
        preco_pagar = kwh * 0.55
    else:
        preco_pagar = kwh * 0.60
else:
    print('ERROR! Insira o tipo de instalação corretamente, sendo residência, indústria ou comércio.')

print('-'*30)
print(f'Tipo: {tipo}\n'
      f'Kwh: {quant_kwh}\n'
      f'Preço a Pagar: R${preco_pagar:.2f}')
