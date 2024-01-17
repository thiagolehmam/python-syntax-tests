'''
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.
'''
nome = str(input('Digite o seu nome')).strip()
nome = nome.split()
print('prazer em conhece-lo')
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
