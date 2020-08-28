# Desafio 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

nc = str(input('Digite seu nome completo: '))
teste = 'Silva' in nc
if teste == True:
    print('Você tem Silva no nome!')
else:
    print('Você não tem Silva no nome!')