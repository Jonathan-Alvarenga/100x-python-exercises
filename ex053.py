frase =str(input('digite uma frase: ').upper().strip())
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letras in range(len(junto) - 1, -1, -1):
    inverso += junto[letras]
print('o inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('temos um palíndromo')
else:
    print('não temos um palíndromo')