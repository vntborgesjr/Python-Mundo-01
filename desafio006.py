# Desafio 006 - Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = float(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz2 = numero ** (1/2)
print('O dobro de {} é {}; '
      '\nO triplo de {} é {}; e '
      '\nA raiz quadrada de {} é {:.2f}.'.format(numero, dobro, numero, triplo, numero, raiz2))

# alternativa para economizar memória

numero = float(input('Digite um número: '))
print('O dobro de {} é {}; '
      '\nO triplo de {} é {}; e '
      '\nA raiz quadrada de {} é {:.2f}.'.format(numero, (numero * 2), numero, (numero * 3), numero, pow(numero, 1/2)))
