# Desasfio 035 - Desenvolva um programa que leia o comprimento de três retas e diga ao usário se elas podem ou não
# formar um triângulo.

print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
r1 = float(input('Digite o comprimento do primeiro lado do triâgulo: '))
r2 = float(input('Digite o comprimento do segundo lado do triângulo: '))
r3 = float(input('Digite o comprimento do terceiro lado do triângulo: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas de comprimento {}cm, {}cm e {}cm podem formar um triângulo.'. format(r1, r2, r3))
else:
    print('As retas de comprimento {}cm, {}cm e {}cm não podem formar um triângulo.'.format(r1, r2, r3))