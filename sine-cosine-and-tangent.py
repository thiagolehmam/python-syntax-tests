'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo = float(input('digite um angulo: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o valor de seno do angulo {} é: {}'.format(angulo,seno))
print('o valor de cosseno do angulo {} é:{}'.format(angulo,coseno))
print('o valor de tangente do angulo {} é:{}'.format(angulo,tangente))
