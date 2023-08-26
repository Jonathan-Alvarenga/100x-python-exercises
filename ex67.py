#Exercício Python 67: Faça um programa que mostre a
# tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário.
# O programa será interrompido quando o número
# solicitado for negativo.

valor = 0
while True:
    valor = int(input('Quer ver a tabuada de qual valor?'))
    print('-' * 30)
    if valor < 0:
        break
    for c in range (1,11):
        print(f'{valor} x {c} = {valor*c}')
    print('-' * 30)
print(f'Programa tabuada encerrado!')
