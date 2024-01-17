'''
Crie um programa que leia o nome
completo de uma pessoa e mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.
'''

nome = str(input('digite seu nome completo')).strip()
print('analisando seu nome...')
print('seu nome em maiusculas é {}'.format(nome.upper()))
print('seu nome em minisculas é: {}'.format(nome.lower()))
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem {} letras'.format(nome.find(' ')))


separa = nome.split()
print('seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))

