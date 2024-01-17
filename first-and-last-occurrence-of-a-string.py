'''
Faça um programa que leia uma frase pelo teclado e
mostre quantas vezes aparece a letra “A”,
em que posição ela aparece a primeira vez e
em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frase:')).upper().strip()
print('a letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('a primeira letra A apareceu na posição {}'.format((frase.find('A')+1)))
print('a ultima letra A apareceu na posição {}'.format((frase.rfind('A')+1)))
