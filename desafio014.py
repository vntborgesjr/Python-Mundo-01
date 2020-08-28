# Desafio 014 - Escreva um programa que que converta uma temperatura digitada em graus Celsius para
# Fahrenheit.

c = float(input('Digite uma temperatura em °C: '))
f = c * 9/5 + 32
print('A temperatura de {:.2f}°C corresponde a {:.2f}°F.'.format(c, f))