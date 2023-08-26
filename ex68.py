#Exercício Python 68: Faça um programa que
# jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.

from random import randint
print('VAMOS JOGAR PAR OU ÍMPAR ')
print('=-'*30)
v = 0
while True:
    player = int(input('Digite um número:'))
    pc = randint(0,10)
    total = player + pc
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]')).strip().upper()[0]
    print(f'Você jogou {player} e o computador jogou {pc}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
