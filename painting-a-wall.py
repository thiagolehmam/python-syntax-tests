'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

'''


largura = float(input('largura da parede: '))
altura = float(input('altura da parede: '))
area= largura*altura
tinta = area/2

print('sua parede tem a dimensão de {:.0f}x{:.0f} e sua area é de {},, para pintar a parede você precisará de {}l de tinta.'.format(largura,altura,area,tinta))

'''


'''
