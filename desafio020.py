# Desafio 020 - O mesmo professor que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos alunos e mostre a ordem sorteada.

'''a = str(input('Digite o nome do primero aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
from random import sample
alunos = [a, b, c, d]
print('A ordem de apresentação dos trabalhos será: \n{}.'.format(sample(alunos, 4)))'''

a = str(input('Digite o nome do primero aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
from random import shuffle
alunos = [a, b, c, d]
shuffle(alunos)
print('A ordem de apresentação dos trabalhos será: \n{}'.format(alunos))
