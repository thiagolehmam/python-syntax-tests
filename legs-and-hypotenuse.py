'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa.
'''

cateto_oposto = float(input('cateto oposto: '))
cateto_adjacente = float(input('cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('a hipotenusa é: {}'.format(hipotenusa))
