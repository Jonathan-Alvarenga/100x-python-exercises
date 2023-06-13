# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar .
# considere US$1,00 = R$4,92.

reais = float(input('Quanto dinheiro você tem na carteira? : R$ '))
dollars = reais / 4.92
euro = reais / 5.31
iene = reais / 0.035
peso = reais / 0.020
print('Com R${:.2f} , você pode comprar US${:.2f} dólares'.format(reais,dollars))
print('Com R${:.2f} , você pode comprar JPY${:.2f} ienes'.format(reais, iene))
print('Com R${:.2f} , você pode comprar EUR${:.2f} euros'.format(reais,euro))
print('Com R${:.2f} você pode comprar ARS${:.2f} pesos argentinos'.format(reais,peso))
