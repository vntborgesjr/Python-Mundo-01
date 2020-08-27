# Desafio 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é par ou impar.

n = int(input("Digite um número inteiro: "))
if n % 2 == 0:
    print('O número \033[1;34m{}\033[m é \033[1;34mpar\033[m.'.format(n))
else:
    print('O número \033[1;31m{}\033[m é \033[1;31mimpar\033[1;31m.'.format(n))