velocidade = int(input('Qual a velocidade do carro em km :'))

multa = 7.00 * velocidade

if velocidade >80:
    print(f'Sua velocidade foi de {velocidade}km você foi multado!! \n'
          f'O valor da multa é de R${multa}')
else:
    print('Continue dirigindo corretamente')