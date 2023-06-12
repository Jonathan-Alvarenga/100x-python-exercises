#Faça um programa que leia o nome completo de uma pessoa , mostrando em seguida o primeiro
# e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro : Ana
# último : Souza

nome = str(input('Digite seu nome inteiro : ')).strip()
nomeD = nome.split()
print('Primeiro nome : {} '.format(nomeD[0]))
print('Ultimo nome : {}'.format(nomeD[len(nomeD)-1]))
