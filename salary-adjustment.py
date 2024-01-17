'''
Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1250,00,
 calcule um aumento de 10%. Para os inferiores ou iguais,
 o aumento é de 15%.
'''

salario = float(input('Qual o seu salario ? '))

print('O salário é: R${:.2f}'.format(salario))
porcentagem = 0
if salario <= 1250:
    porcentagem = 15
    novo= salario + (salario* porcentagem / 100)
else:
    porcentagem = 10
    novo= salario + (salario * porcentagem / 100)

print('Você ganhava R${:.2f} agora vai ganhar R${:.2f}, foi um aumento de {}%'.format(salario,novo,porcentagem))
