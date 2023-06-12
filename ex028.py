#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
pc = randint(0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
player = int(input('Em que número eu pensei ? :'))
if pc == player:
    print('PARABÉNS! Você me venceu!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}.'.format(pc,player))
