#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

cel = float(input('Graus Celsius : '))
fah = cel * 1.8 + 32
print('{:.1f}Cº é equivalente á {:.1f}Fº'.format(cel,fah))
