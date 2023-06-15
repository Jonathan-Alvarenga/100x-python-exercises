#Exercício Python 37: Escreva um programa em Python que leia um número inteiro
# qualquer e peça para o usuário escolher
# qual será a base de conversão:
# 1 para binário,
# 2 para octal e
# 3 para hexadecimal.


print('CONVERSOR DE NÚMEROS [...]')
num = int(input('Digite um número para converter :'))
print('Escolha a opção a seguir :')
print('[1] = Binário')
print('[2] = Octal')
print('[3] = Hexadecimal')
op = int(input('Opção :'))
if op == 1:
    print('\33[1:31mBinário = {}\33[m'.format(bin(num)[2:]))
    print('CONVERTIDO [...]')
elif op == 2:
    print('\33[1:32mOctal = {}\33[m'.format(oct(num)[2:]))
    print('CONVERTIDO [...]')
elif op == 3:
    print('\33[1:34mHexadecimal = {}\33[m'.format(hex(num)[2:]))
    print('CONVERTIDO [...]')
else:
    print('Opção inválida, tente novamente!')







