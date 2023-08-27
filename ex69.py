#Exercício Python 69: Crie um programa que leia a
# idade e o
# sexo de várias pessoas.
# A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

#A) quantas pessoas tem mais de 18 anos.

#B) quantos homens foram cadastrados.

#C) quantas mulheres tem menos de 20 anos.
maiorIdade = menorIdade = homens = mulherNova = 0
while True:
    idade = int(input('Digite sua idade :'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
    if idade >= 18:
        maiorIdade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulherNova += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if op == 'N':
        break
print(f'Foram computados {maiorIdade} pessoas maiores de 18 anos , sendo {homens} homens e {mulherNova} mulheres com menos de 20 anos.')
