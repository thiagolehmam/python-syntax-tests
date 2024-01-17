'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
que o carro custa R$60 por dia e R$0,15 por Km rodado.
'''

km_percorridos = float(input('qual a quantidade de km percorridos ? '))
dias_alugados = float(input('quais a quantidade de dias alugadors ? '))
preco_a_pagar = (dias_alugados * 60) + (0.15 * km_percorridos)
print('como foram percorridos {}km em {} dias de uso o total a ser pago é: {}'.format(km_percorridos, dias_alugados, preco_a_pagar))
print(dias_alugados)
