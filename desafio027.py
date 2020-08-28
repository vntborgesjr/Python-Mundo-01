# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o segundo nome
# separadamente

nc = str(input('Digite seu nome completo: ')).strip().split()
print('Seu primeiro nome é {}'.format(nc[0]),
      '\nSeu último nome é {}'.format(nc[len(nc) - 1]))