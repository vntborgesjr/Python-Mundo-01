# Desafio 013 - Faça um algoritmo que leia o salário de um funcionário e mostr seu novo slaário, com 15%
# de aumento.

salario = float(input('Informe o valor do salário: R$'))
novo = salario + salario * 0.15
print('O novo salário com 15% de aumento será R${:.2f}'.format(novo))