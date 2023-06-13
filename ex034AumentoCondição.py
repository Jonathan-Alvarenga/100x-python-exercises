#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input("Digite o valor do seu salário R$ : "))
if sal >= 1250:
    novo = (sal * 0.10) + sal
else:
    novo = (sal * 0.15) + sal
print('Salário antigo R${:.2f}, novo salário R${:.2f}'.format(sal,novo))


