'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

n = int(input('digite a primeira nota'))
n2= int(input('digite a segunda nota:'))
media = (n+n2)/2
print('a media entre {} e {} é {}'.format(n,n2,media ))

print('Parabéns' if media >= 6 else 'Estude Mais')