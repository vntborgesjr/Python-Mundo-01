# Curso de Python 01 - aula 010 - Condições simples e compostas (Parte 1)
'''if condição:
        bloco True
    else:
        bloco False'''

'''tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro  novo')
else:
    print('carro velho')
print('Fim')

# ou
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')'''

'''nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))'''

'''nome = str(input('Qual é o seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))'''

'''n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a secunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a secunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}.'.format(m))
print('PARABÉNS!' if m >= 6.0 else 'Estude mais!')