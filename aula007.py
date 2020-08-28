# alinhando a esquerda
nome = 'Vitor Borges'
print('Olá {:<20}!'.format(nome))

# alinhado a direita
print('Olá {:>20}!'.format(nome))

# centralizado
print('Ola {:^20}!'.format(nome))

# realizando operações aritméticas e arredondando valores
n1 = 9
n2 = 2
s = n1 + n2
d = n1 / n2
m = n1 * n2
d1 = n1 // n2
e = n1 ** n2
print('A soma é {}, a divisão é {:.2f} e o produto é {}.'.format(s, d, m), end = ' ') # o argumento end = '' evita
# que o python pule a linha para imprimir o próxim print()
print('A divisão inteira é {} e a potência é {}.'.format(d1, e))

# o argumento end = '' evita que o python pule a linha para imprimir o próxim print()
print('A soma é {}, a divisão é {:.2f} e o produto é {}.'.format(s, d, m), end = ' ') # o argumento end = '' evita
# que o python pule a linha para imprimir o próxim print()
print('A divisão inteira é {} e a potência é {}.'.format(d1, e))

# a \n indica ao python que ele pule para a próxima linha para continuar imprimindo a mensagem
print('A soma é {}, \n a divisão é {:.2f} e \n o produto é {}.'.format(s, d, m), end = ' ') # o argumento end = '' evita
# que o python pule a linha para imprimir o próxim print()
print('A divisão inteira é {} e \n a potência é {}.'.format(d1, e))

