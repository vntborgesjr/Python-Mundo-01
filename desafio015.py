# Desafio 015 - Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60,00
# por dia e R$0,15 por km rodado.

d = int(input("Digite o número de dias de aluguel: "))
km = float(input('Digite os km rodados: '))
p = (d * 60) + (km * 0.15)
print('O aluguel do carro por {} dias que percorreu {:.2f}km custa R${:.2f}'.format(d, km, p))