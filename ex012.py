# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.

p = int(input('Digite o valor : '))
d = int(input('Digite o desconto : '))
cal = (d * p ) / 100
vl = p - cal
print('Valor com desconto : {}'.format(vl))
