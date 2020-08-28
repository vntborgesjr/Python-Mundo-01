# Desafio 010 - crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela
# pode comprar. Considere US$1.00 = R$3.27

real = float(input('Digite o valor em reais: R$'))
dolar = real / 3.27
print('A quantia de R${:.2f} corresponde a US${:.2f}.'.format(real, dolar))