'''
 Faça um programa que leia um número de 0 a 9999
 e mostre na tela cada um dos dígitos separados.
'''
num = int(input('Informe um numero: '))
n = str(num)
print('analisando o numero {} '.format(num))
print('unidade: {} '.format(n[3]))
print('dezena: {} '.format(n[2]))
print('centena: {} '.format(n[1]))
print('milhar: {} '.format(n[0]) )
