# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar .
# considere US$1,00 = R$3,27.

reais = float(input('Digite a quantia em Reais : '))
dollars = reais // 3.27
print('Você consegue comprar {} dólares'.format(dollars))
