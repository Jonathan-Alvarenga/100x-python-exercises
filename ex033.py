#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

a = int(input('primeiro número :'))
b= int(input('segundo número :'))
c= int(input('terceiro número :'))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('o menor número é {}'.format(menor))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o maior número é {}'.format(maior))
