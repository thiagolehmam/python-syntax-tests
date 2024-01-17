'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('qaul o seu salario ? '))
print('O salário é: R${:.2f}'.format(salario))
novo= salario + (salario*0.15)
print('O seu novo salário com 15% de aumento será: R${:.2f}'.format(novo))
