# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# - o nome com todas as letras maiúsculas
# - o nome com todas as letras minúsculas
# - quantas letras ao todo, sem consolidar espaços
# - quantas letras tem o primeiro nome

nc = str(input('Digite seu nome completo: '))
print('Todas as letras maiúsculas: ', nc.upper(),
      '\nTodas as letras minúsculas: ', nc.lower(),
      '\nNúmero total de letras, sem espaços (.count()): ', len(nc) - nc.count(' '),
      '\nNúmero total de letras, sem espaço (.replace()): ', len(nc.replace(' ', '')),
      '\nO primeiro nome é {} tem {} letras (.split()).'.format(nc.split()[0], len(nc.split()[0])),
      '\nO primeiro nome tem {} letras (.find()).'.format(nc.find(' ')))