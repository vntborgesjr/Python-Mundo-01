# Desafio 008 - Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite um valor em metros: '))
cm = m * 100
mm = m * 1000
print('O valor de {}m corresponde a {}cm e {}mm.'.format(m, cm, mm))

# alternativa

m = float(input('Digite um valor em metros: '))
print('O valor de {}m corresponde a {}cm e {}mm.'.format(m, m * 100, m * 1000))

# alternativa

m = float(input('Digite um valor em metros: '))
print('A medida de {}m corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm'.format(m, m/1000, m/100,
                                                                                               m/10, m*10,
                                                                                         m * 100, m * 1000))

