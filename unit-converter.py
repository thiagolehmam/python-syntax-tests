'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
'''

n = float(input('uma distancia em metros: '))
print('a medida {}m corresponde a:'.format(n))


print(n/100, 'hm')
print(n/10, 'dam')
print('{:.0f}dm'.format(n*10))
print('{:.0f}cm'.format(n*100))
print('{:.0f}mm'.format(n*1000))
