# Faça um programa que leia o salário de um fucionário e mostre seu novo salário , com 15% de aumento.

salario = float(input('Digite o salário : '))
novoSalario = salario + (salario * 15 / 100)
print('Novo salário com 15% de aumento : {:.2f} '.format(novoSalario))
