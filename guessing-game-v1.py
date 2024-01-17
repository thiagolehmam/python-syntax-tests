'''
Escreva um programa que faça o computador “pensar” em um número inteiro
entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
escolhido pelo computador. O programa deverá escrever na tela se o usuário
venceu ou perdeu.
'''

from random import randint
from time import sleep

computador = randint(0,5)

print('-='*25)
print('Pensei em um número entre 0 e 5. tente advinhar...  ')
print('-='*25)
jogador = int(input('Em qual número eu pensei ???'))
print('processando...')
sleep(2)

if computador == jogador:
    print('PARABEÉNS! Você Ganhou!')
else:
    print('Você Perdeu!')
    print('Eu pensei no numero {}'.format(computador))
