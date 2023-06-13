# Exercício Python 18: Faça um programa que leia um ângulo
# qualquer e mostre na tela o valor do seno, cosseno e
# tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo : '))
sen = sin(radians(angulo))
cos = cos(radians(angulo))
tan = tan(radians(angulo))
print('Valor no seno : {:.2f} \nValor do cosseno : {:.2f} \nValor da tangente : {:.2f}'.format(sen, cos, tan))
