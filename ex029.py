#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

vel = int(input('Velocidade no radar : '))
if vel >= 80:
    print('Você foi multado! ')
    multa = vel - 80
    print('Máximo permitido é 80km/h , você ultrapassou o radar em {}km/h acima do permitido.'.format(multa))
    print('Valor da multa : R${:.2f}'.format(float(multa * 7.00)))
else:
    print('Você não foi multado!')
