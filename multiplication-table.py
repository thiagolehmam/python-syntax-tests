'''Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
'''
n = int(input('Digite um número para ver sua tabuada: '))
print('-'*15)
for c in range (1,11):
    print('{} x 1 = {}'.format(c,n*c))

print('-'*15)