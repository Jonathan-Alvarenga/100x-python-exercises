# Crie um programa que leia o nome
# de uma cidade e diga se ela começa ou não com a palavra "SANTO".

cid = str(input('Digite o nome de uma cidade : '))
print(cid[:5].upper() == 'SANTO')
