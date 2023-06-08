# Crie um algorítimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))
dobro = n * 2
triplo = n * 3
raiz = pow(n, (1/2))
print('Seu dobro é {}, seu triplo é {} e sua raiz quadrada é {:.2f} !'.format(dobro,triplo,raiz))
