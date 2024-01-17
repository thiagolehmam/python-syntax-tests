'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''
preco = float(input('qual o preço do produto para apliicar o desconto de 5% ? '))
novo = preco - (preco*0.05)
print('O preço antigo que era R${:.2f}, agora é R${:.2f} com a aplicação do desconto de 5%'.format(preco,novo))
