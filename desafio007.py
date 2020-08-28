# Desafio 007 - Desenvolva um programa que leia as duas notas de um aluno, calcule e mostr a sua média.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('A média entre {:.1f} e {:.1f} foi {:.1f}'.format(nota1, nota2, media))

# alternativa 1 - evitando a criação de variável para economizar memória

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
print('A média entre {:.2f} e {:.2f} foi {:.2f}'.format(nota1, nota2, ((nota1 + nota2)/2)))
