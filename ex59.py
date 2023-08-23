#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

numero = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
op = 0
while op != 5:
    print('Digite a opção desejada\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa ')
    op = int(input(''))
    if op == 1:
        soma = numero + numero2
        print('A soma dos números {} e {} é {}'.format(numero,numero2,soma))
    elif op == 2:
        produto = (numero * numero2)
        print('O produto da multiplicação entre {} e {} é {}'.format(numero,numero2,produto))
    elif op == 3:
        if numero > numero2:
            print('O maior número digitado foi {}'.format(numero))
        else:
            print('O maior número digitado foi {}'.format(numero2))
    elif op == 4:
        numero = int(input('Digite um novo número:'))
        numero2 = int(input('Digite um novo segundo número:'))
    elif op > 5:
        print('Opção inválida , tente novamente :')
print('Finalizado.')




