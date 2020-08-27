# Desafio 028 - Escreva um programa que faça o computador 'pensar' em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

print('-=-' * 20)
print('Vou pensar em um número entre 0 a 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO')
from random import randint
pc = randint(0, 5)
from time import sleep
sleep(3)
if n == pc:
    print('\033[1;32mParabéns!\033[0;32m Você acertou o número!')
else:
    print('\033[1;31mDessa vez errou o número. Eu pensei no número {} e não no {}. '
          '\n\033[mTente novamente.'.format(pc, n))