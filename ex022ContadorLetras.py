# Crie um programa que leia o nome de uma pessoaa e mostre:
# O nome com todas as letras maiúsculas
#O nome com todas as letras minúusculas
# Quantas letras ao Todo sem considerar espaços
# Quantas letras tem o primeiro nome .

nome = str(input('Escreva seu nome inteiro : ')).strip()
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo contém {} letras'.format(len(nome)-nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele contém {} letras'.format(separa[0],len(separa[0])))
