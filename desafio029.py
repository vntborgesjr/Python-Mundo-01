# Desafio 029 - Escreva um progama que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem
# dizendo que ele foi multado. A multa vai custar R$7,00 por cada km/h acima do limite.

v = int(input('Informe a velocidade do veículo: '))
if v > 80:
    print('O seu veículo foi \033[4;31mMULTADO\033[m.'
          '\nVocê excedeu o limite permitido que é de \033[7;30;41m80km/h\033[m.'
          '\nO valor da multa é de \033[4;31mR${:.2f}\033[m.'.format(float(7 * (v - 80))))
else:
    print('Tenha um bom dia! '
          '\nA velocidade de \033[4;34;40m{}km/h\033[m está dentro do limite permitido.'
          '\nDirija com segurança!'.format(v))