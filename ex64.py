#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

xnumeros = soma = num = 0
num = int(input('Digite vários números e use 999 para sair :'))
while num != 999:
    soma += num
    xnumeros += 1
    num = int(input('Digite vários números e use 999 para sair :'))
print('{} números digitados e a soma foi de {}'.format(xnumeros, soma))


