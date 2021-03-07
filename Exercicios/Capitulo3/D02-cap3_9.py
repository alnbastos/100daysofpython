"""
(17/02/2021) Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário.
Calcule o total em segundos.
"""
print('\033[34mCONVERSÃO PARA SEGUNDOS\033[m')
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

conv_dias = dias * 86400
conv_horas = horas * 3600
conv_minutos = minutos * 60

soma = conv_dias + conv_horas + conv_minutos + segundos

print(f'A soma dos dias, horas, minutos e segundos informados, dão o total de \033[34m{soma} segundos.\033[m')
