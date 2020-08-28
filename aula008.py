from math import sqrt
n = int(input('Digite um número: '))
print('A raiz quadrada de {} é {:.2f}'.format(n, sqrt(n)))

import random
num = random.random()
print('{:.2f}'.format(num))
n2 = random.randint(1, 10)
print('{}'.format(n2))

import emoji
print(emoji.emojize('Olá, Mundo! :sunglasses:', use_aliases = True))
print(emoji.emojize('Olá, Mundo! :earth_americas:', use_aliases = True))