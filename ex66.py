#Exercício Python 66: Crie um programa que leia números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final,
# mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

quant = soma = 0
while True:
    n = int(input('Digite um número: [999 para finalizar]'))
    if n == 999:
        break
    soma += n
    quant += 1
print(f'Foram digitados {quant} números e a soma foi de {soma}')
