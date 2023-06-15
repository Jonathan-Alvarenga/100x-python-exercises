#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

#– IMC abaixo de 18,5: Abaixo do Peso

#– Entre 18,5 e 25: Peso Ideal

#– 25 até 30: Sobrepeso

#– 30 até 40: Obesidade

#– Acima de 40: Obesidade Mórbida

peso = float(input('qual é o seu peso ? (Kg)  :'))
altura = float(input('qual é a sua altura ? (m) :'))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('Seu IMC é : {:.2f}'.format(imc))
    print('IMC abaixo de 18,5 : Abaixo do peso.')
elif imc <= 25:
    print('Seu IMC é : {:.2f}'.format(imc))
    print('IMC entre 18.5 e 25 : Peso ideal.')
elif imc <= 30:
    print('Seu IMC é : {:.2f}'.format(imc))
    print('IMC entre 25 e 30 : Sobre peso.')
elif imc <= 40:
    print('Seu IMC é : {:.2f}'.format(imc))
    print('IMC entre 30 e 40 : Obesidade.')
else:
    imc >= 40
    print('Seu IMC é : {:.2f}'.format(imc))
    print('IMC acima de 40 : Obesidade mórbida')