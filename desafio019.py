# Desafio 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
# que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

'''a = str(input('Digite o nome do primero aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
from random import sample
alunos = (a, b, c, d)
print('O aluno sorteado para apagar o quadro foi {}.'.format(sample(alunos, 1)))'''

a = str(input('Digite o nome do primero aluno: '))
b = str(input('Digite o nome do segundo aluno: '))
c = str(input('Digite o nome do terceiro aluno: '))
d = str(input('Digite o nome do quarto aluno: '))
from random import choice
alunos = [a, b, c, d]
print('O aluno sorteado para apagar o quadro foi {}.'.format(choice(alunos)))

