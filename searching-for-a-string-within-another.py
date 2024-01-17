'''
 Crie um programa que leia o nome de uma pessoa
 e diga se ela tem “SILVA” no nome.
'''
nome = str(input('Qual o seu nome competo? ')).strip()
print('seu nome tem silva? {}'.format('silva' in nome.lower()))

