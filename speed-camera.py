'''
 Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
 que ele foi multado. A multa vai custar R$7,00 por
 cada Km acima do limite.
'''
limite_velocidade = 80

velocidade = int(input('qual a velocidade ?'))

if velocidade > limite_velocidade:
    print('MULTADO! Você excedeu o limite permitido que é de {}km'.format(limite_velocidade))
    print('Você deve pagar uma multa de R${}'.format((velocidade - limite_velocidade)*7 ))
    print('Tenha um bom dia! Dirija com Segurança!')
else:
    print('DENTRO DO LIMITE! Tenha um bom dia! Dirija com Segurança!')
