# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.

n = input('digite algo:')
print(type(n))
print ('É alfanumérico ?',n.isalpha())
print ('É minúsculo ?', n.islower())
print ('É decimal ?',n.isdecimal())
print ('É um título ?',n.istitle())

