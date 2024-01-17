'''
O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''
from random import shuffle
a1 = input('aluno 1:')

a2 = input('aluno 2:')

a3 = input('aluno 3:')

a4 = input('aluno 4:')

alunos = [a1,a2,a3,a4]

escolhido = shuffle(alunos)
print('A ordem de apresentação de trabalhos dos alunos será: 1º {}, 2º {}, 3º {} e 4º {}'.format(alunos[0],alunos[1],alunos[2],alunos[3]
))

