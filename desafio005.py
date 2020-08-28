# Desafio 005 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

inteiro = int(input('Digite um número inteiro: '))
antecessor = inteiro - 1
sucessor = inteiro + 1
print('O antecessor de {} é {}. \nO sucessor de {} é {}.'. format(inteiro, antecessor, inteiro, sucessor))

# alternativa 1

inteiro = int(input('Digite um número inteiro: '))
print('O antecessor de {} é {}. \nO sucessor de {} é {}.'. format(inteiro, (inteiro - 1), inteiro, (inteiro + 1)))

# quanto menos variável for utilizada, mais memória será economizada