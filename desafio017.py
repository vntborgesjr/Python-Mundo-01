# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
# retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa de um triângulo cujo cateto oposto é {} e o cateto adjacente é {} será de {:.2f}'
      .format(co, ca, sqrt(pow(co, 2) + pow(ca, 2))))

# alternativa 1

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('O valor da hipotenusa de um triângulo cujo cateto oposto é {} e o cateto adjacente é {} será de {:.2f}'
      .format(co, ca, hypot(co, ca)))
