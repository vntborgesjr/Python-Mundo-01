# Desafio 032 - Faça um programa que leia um ano qualuqer e mostra se ele é bissexto.

from datetime import date
a = int(input('Digite um ano. Coloque 0 para analisar o ano atual: '))
if a == 0:
    ano = date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("O ano {} é bissexto!".format(a))
else:
    print('O ano {} não é bissexto!'.format(a))