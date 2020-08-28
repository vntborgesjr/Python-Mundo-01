# faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as
# informações possíveis sobre ele

x = input('Digite algo: ')
print('O tipo primitivo deste valor é ', type(x))
print('Só tem espaços? ', x.isspace())
print('É um número? ', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico? ', x.isalnum())
print('É maiúscula? ', x.isupper())
print('É minúscula?', x.islower())
print('E capitalizada?', x.istitle())