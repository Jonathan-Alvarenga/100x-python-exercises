#Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar. A prestação mensal
# não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa: R$'))
salario = float(input('Quanto é o seu salário: R$'))
anos = int(input('Quantos anos você vai pagar: '))
parcela = casa / (anos * 12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(casa, anos,parcela ))
if parcela <= salario * 0.30:
    print('\33[1:32mEmpréstimo aprovado!\33[m')
else:
    parcela >= salario * 0.30
    print('\33[1:31mEmpréstimo negado!\33[m')



