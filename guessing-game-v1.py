'''
Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
'''

from random import randint

computador = randint(0,5)

jogador = int(input('Qual o número você escolhe entre 1 e 5 ? '))

if computador == jogador:
    print('você ganhou')
else:
    print('você perdeu!')
    print('pensei no numero {}'.format(computador))
