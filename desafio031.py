# Desafio 031 - Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

d = float(input('Informa a distância da viagem: '))
if d <= 200:
    print('Para uma viagem de {}km a passagem custa R${}.'.format(d, d * 0.5))
else:
    print('Para uma viagem de {}km a passagem custa R${}.'.format(d, d * 0.45))