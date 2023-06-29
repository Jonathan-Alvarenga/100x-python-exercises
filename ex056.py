#Exercício Python 56: Desenvolva um programa que leia o
# nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

soma = 0
maiorIdadeHomem = 0
contadorMulheres = 0
nomeHomemVelho = ''
for c in range(1,5):
    print('---- {}° PESSOA -----'.format(c))
    nome = str(input('Nome: ').strip())
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ').upper().strip())
    soma += idade
    if c == 1:
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    if sexo == 'M' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeHomemVelho = nome
    if sexo == 'F' and idade > 20:
        contadorMulheres += 1
print('o nome do homem mais velho é {} e tem {} anos'.format(nomeHomemVelho,maiorIdadeHomem))
print('existem {} mulheres com mais de 20 anos'.format(contadorMulheres))
print('A média de idade das 4 pessoas é {}'.format(soma / 4))

