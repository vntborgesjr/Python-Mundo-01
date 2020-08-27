# Desafio 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores a R$1.250,00, calucule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Informe o saçário do funcionário: R$'))
if s > 1250:
    print('O novo salário com um aumento de 10% será de R${:.2f}.'.format(s +(s*0.1)))
else:
    print('O novo salário com uma aumento de 15% será de R${:.2f}.'.format(s + (s*0.15)))