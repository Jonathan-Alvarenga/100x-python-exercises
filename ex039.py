#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua
# idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa
# também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime
ano = int(input('que ano você nasceu? :'))
atual = datetime.date.today().year
idade = atual - ano
print('quem nasceu em {} tem {} anos em {}.'.format(ano,idade,atual))
if atual - ano < 18:
    print('você deverá  se alistar em {} anos'.format(18-idade))
    print('seu alistameneto será em {}.'.format(ano+18))
elif atual - ano > 18:
    print('seu alistamento foi em {}'.format(ano + 18))
else:
    atual - ano == 18
    print('aliste-se já !')



