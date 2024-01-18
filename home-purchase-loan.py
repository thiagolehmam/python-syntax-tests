'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

valor_casa = float(input('Qual o valor da casa ? '))
salario_comprador = float(input('Qual o salário do comprador da casa ? '))
pagamento = int(input('Em quantos anos pretende pagar o emprestimo ? '))

meses_pagamento = pagamento*12

prestacao_mensal = valor_casa/meses_pagamento


print('Para pagar uma casa de R${:.2f} em {} anos.'.format(valor_casa,pagamento),end=' ')
print('A prestação será de R${:.2f}.'.format(prestacao_mensal))


if prestacao_mensal < (salario_comprador*(30/100)):
    print('emprestimo aprovado')
else:
    print('emprestimo negado')

