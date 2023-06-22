#Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.
primeiro = int(input('digite o primeiro termo :'))
razao = int(input('digite a razão :'))
décimo = primeiro + (10 - 1) * razao
for c in range(primeiro, décimo + razao, razao):
    print('{}'.format(c), end=' - ')
print('ACABOU')


