# Desafio 3 - Crie um script python que leia dois números e tente mostrar a soma
# entre eles
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A resultado de', n1, '+', n2, '=', n1 + n2)

# Aperfeiçoando o código da mensagem final

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A resultado de {} + {} = {}!' .format(n1, n2, n1+n2))