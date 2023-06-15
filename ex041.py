#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

#– Até 9 anos: MIRIM

#– Até 14 anos: INFANTIL

#– Até 19 anos: JÚNIOR

#– Até 25 anos: SÊNIOR

#– Acima de 25 anos: MASTER

import datetime
ano = int(input('ano de nascimento :'))
atual = datetime.date.today().year
idade = atual - ano
print('você tem {} anos'.format(idade))
if idade <= 9:
    print('até 9 anos : mirim')
elif idade <= 9:
    print('até 14 anos : infantil')
elif idade <= 14:
    print('até 19 anos : júnior')
elif idade <= 19:
    print('até 25 anos : sênior')
else:
    idade > 25
    print('acima de 25 anos : master')
