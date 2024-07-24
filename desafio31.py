kms = int(input('Digite a distancia em km da sua viagem :'))

vlr1 = kms*0.50
vlr2 = kms*0.45

print('CALCULANDO...')

if kms <=200:
    print(f'O valor total da passagem é de R${vlr1}')
else:
    print(f'O valor total da passagem é de R${vlr2}')
print('Obrigado pela sua preferência!!')
