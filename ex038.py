#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

#– O primeiro valor é maior

#– O segundo valor é maior

#– Não existe valor maior, os dois são iguais

num1 = int(input('primeiro número :'))
num2 = int(input('segundo número :'))
if num1 < num2:
    print('o número {} é maior'.format(num2))
elif num1 > num2:
    print('o número {} é menor'.format(num2))
else:
    num1 == num2
    print('não exixte valor maior , os dois são iguais')
