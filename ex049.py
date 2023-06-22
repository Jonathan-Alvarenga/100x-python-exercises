#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um
# número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Digite um número para mostrar sua tabuada :'))
for c in range(1,11):
    print('{} X {} = {}'.format(numero, c, numero * c))

