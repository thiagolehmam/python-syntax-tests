'''
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais

'''

valor1 = int(input('digite um valor inteiro: '))

valor2 = int(input('digite outro valor inteiro a ser comparado: '))

if valor1 > valor2:
    print('O primeiro valor é maior')
elif valor2 > valor1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')
