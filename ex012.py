# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.

produto = int(input('Digite o valor : '))
desconto = int(input('Digite o desconto : '))
cal = (desconto * produto ) / 100
vl = produto - cal
print('Valor com desconto : {}'.format(vl))
