# Faça um programa que leia o salário de um fucionário e mostre seu novo salário , com 15% de aumento.

salario = float(input('Digite o salário : '))
calculo = salario * 0.15
novoSalario = salario + calculo
print('Novo salário com 15% de aumento : {} '.format(novoSalario))
