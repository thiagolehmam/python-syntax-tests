'''
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
'''
numero = int(input('digite um número inteiro a ser convertido: '))
print('-'*30)
print('Qual a Base de Conversão ?')
print('-'*30)
print('''
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal
''')
print('-'*30)

escolha = int(input('digite a escolha: '))

if escolha == 1:

    print('{} em binário é {} '.format(numero,bin(numero)[2:]))
elif escolha == 2:
    print('{} em octal é {} '.format(numero,oct(numero)[2:]))
elif escolha==3:
    print('{} em hexadecimal é {} '.format(numero,hex(numero)[2:]))
else:
    print('escolha invalida')




