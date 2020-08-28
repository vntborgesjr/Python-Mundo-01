# Desafio 009 - Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

inteiro = int(input('Digite um número inteiro: '))
print('-' * 12)
for i in range(0, 11):
    print('{} x {:2} = '.format(inteiro, i), i * inteiro )
print('-' * 12)
