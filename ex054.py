#Exercício Python 54: Crie um programa que
# leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
import datetime
totalMaiores = 0
totalMenores = 0
for c in range(1,8):
    nascimento = int(input('Ano de nascimento da {}° pessoa :'.format(c)))
    if datetime.date.today().year - nascimento >= 18:
        totalMaiores += 1
    else:
        totalMenores += 1
print('Ao todo temos {} pessoas maiores de idade'.format(totalMaiores))
print('E também tivemos {} pessoas menores de idade'.format(totalMenores))
