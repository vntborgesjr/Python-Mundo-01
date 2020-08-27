# Aula 011 - adiicionando cores
# ANSI escape sequence
# para adicionar cores - \033['style text back'm
# ex: \033[0;33;44m
# códigos para estilo: 0, 1, 4 e 7
# 0 == nenhum
# 1 == negrito
# 4 == sublinhado
# 7 == negativo
# códigos para texto: 30 a 37
# códigos para fundo: 40 a 47
# caracter em branco e fundo vermelho: \033[0;30;41m
# caracter em amarelo, sublinahdod e fundo azul: \033[4:33:44m
# caracter em roxo, negrito, e fundo amarelo: \033[1;35;43m
# caracter em branco, fundo verde: \033[30;42m
# caracter em cinza, fundo preto: \033[m
# caracter em preto, fundo branco: \033[7;30m

print('\033[30mOlá, Mundo!') # letra branca
print('\033[31mOlá, Mundo!') # letra vermelha
print('\033[32mOlá, Mundo!') # letra verde
print('\033[33mOlá, Mundo!') # letra amarela
print('\033[34mOlá, Mundo!') # letra azul
print('\033[35mOlá, Mundo!') # letra lilás
print('\033[36mOlá, Mundo!') # letra ciano
print('\033[37mOlá, Mundo!') # letra cinza
print('\033[31;43mOlá, Mundo!') # letra vermelha e fundo amarelo
print('\033[1;31;43mOlá, Mundo!') # letra em negrito, vermelha e fundo amarelo
print('\033[1;31;43mOlá, Mundo!\033[m') # letra em negrito, vermelha e fundo amarelo
print('\033[4;30;45mOlá, Mundo!\033[m') # letra sublinhada, branca e fundo lilas
print('\033[1;31;43mOlá, Mundo!\033[m') # letra em negrito, vermelha e fundo amarelo
print('\033[7;30mOlá, Mundo!\033[m') # letra preta e fundo branco
print('\033[0;33;44mOlá, Mundo!\033[m') # letra amarela e fundo azul
print('\033[7;33;44mOlá, Mundo!\033[m') # letra azul e fundo amarelo
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))
nome = 'Borges'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m',
         'vermelhoepreto': '\033[1;7;31m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelhoepreto'], nome, cores['limpa']))
n = 'Jose'
i = 25
'Você se chama {n} e tem {i} anos de idade'.format(n, i)