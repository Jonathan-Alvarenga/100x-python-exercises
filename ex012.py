# Faça um algorítimo que leia o preço de um produto e mostre seu novo preço , com 5% de desconto.

produto = float(input('Digite o valor : '))
desconto = float(input('Digite o desconto : '))
vl = produto - (desconto * produto ) / 100
print('Valor com desconto : {:.2f}'.format(vl))
