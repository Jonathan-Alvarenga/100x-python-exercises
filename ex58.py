#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
pc = randint(0,10)
c = 1
print('Vou pensar em um número entre 0 e 10. Tente advinhar...')
jogador = int(input('Em que número eu pensei ? :'))
while pc != jogador:
    if jogador < pc:
        jogador = int(input('Mais... Tente novamente!'))
    if jogador > pc:
        jogador = int(input('Menos... Tente novamente!'))
    c += 1
print('Acertou , eu pensei no número {}'.format(pc))
print('Foram {} tentativas até acertar.'.format(c))