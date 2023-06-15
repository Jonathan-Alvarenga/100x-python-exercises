#Exercício Python 040: Crie um programa que leia duas notas de um aluno
# e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:

#– Média abaixo de 5.0: REPROVADO

#– Média entre 5.0 e 6.9: RECUPERAÇÃO

#– Média 7.0 ou superior: APROVADO

nota1 = float(input('nota 1 :'))
nota2 = float(input('nota 2 :'))
media = (nota1 + nota2) / 2
print('média : {}'.format(media))
if media < 5.0:
    print('\33[1:31m REPROVADO!')
elif media > 6.9:
    print('\33[1:32m APROVADO!')
else:
    media > 5.0 and media < 6.9
    print('\33[1:34m RECUPERAÇÃO!')

