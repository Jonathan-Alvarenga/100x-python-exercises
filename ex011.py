# Faça um programa que leia a larfura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la , sabendo que cada litro de tinra pinta uma áerea de 2m².

larg = float(input('Digite a largura da parede : '))
alt = float(input('Digite a altura da parede : '))
area = larg * alt
tinta = area / 2

print('A área da sua parede tem {} m² , exigirá {} litros de tinta. '.format(area, tinta))
