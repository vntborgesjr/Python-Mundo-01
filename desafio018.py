# Desafio 018 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.

from math import sin, cos, tan, radians
a = float(input('Digite um ângulo em graus: '))
print('O seno de {}° é {:.2f}, seu cosseno é {:.2f} e sua tangente é {:.2f}.'.format(a, sin(radians(a)),
                                                                                     cos(radians(a)), tan(radians(a))))