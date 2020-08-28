# Crie um programa que leia o nome de uma cidade e diga se ele começa ou não com o nome 'SANTO'.

cidade = str(input('Digite o nome da sua cidade: ')).lower()
teste = 'santo' in cidade
if teste == True:
    print('O nome da sua cidade começa com Santo.')
else:
    print('O nome da sua cidade não começa com Santo.')
