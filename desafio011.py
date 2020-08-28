# Desafio 011 - Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua área e a
# quatidade de tinta necssária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 m².

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} X {}m. '
      '\nPara pintar uma parede com área de {}m² são necessários {}L de tinta.'.format(altura, largura, area, tinta))