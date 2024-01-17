'''
 Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo
 que ele foi multado. A multa vai custar R$7,00 por
 cada Km acima do limite.
'''
limite_velocidade = 80

velocidade = int(input('qual a velocidade ? '))
print('_'*55)
if velocidade > limite_velocidade:
    print('MULTADO! Você excedeu o limite permitido que é de {}km'.format(limite_velocidade))
    multa = (velocidade - limite_velocidade)*7
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))

else:
    print('DENTRO DO LIMITE!')

print('_'*55)
print('Tenha um bom dia! Dirija com Segurança!')
