'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
from random import choice


alunos = []
nome_aluno1 = input(f"Informe o nome do aluno 1:")
alunos.append(nome_aluno1)

nome_aluno2 = input(f"Informe o nome do aluno 2:")
alunos.append(nome_aluno2)

nome_aluno3 = input(f"Informe o nome do aluno 3:")
alunos.append(nome_aluno3)

nome_aluno4 = input(f"Informe o nome do aluno 4:")
alunos.append(nome_aluno4)

aluno_escolhido = choice(alunos)
print('o aluno escolhido foi: {}'.format(aluno_escolhido))
