# Escreva um programa que leia um valor e exiba convertido em centímetros e milímetros

v = float(input('Digite um valor em metros : '))
cent = v * 100
mili = v * 1000
print(' {} metros são {} centímetros e {} milímetros '.format(v, cent, mili))
