# Faça um programa que leia a larfura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pinta-la , sabendo que cada litro de tinra pinta uma áerea de 2m².

l = int(input('Digite a largura da parede : '))
a = int(input('Digite a altura da parede : '))
ar = l * a
t = ar / 2

print('A área da sua parede é {} m² , exigirá {} litros de tinta. '.format(ar, t))
