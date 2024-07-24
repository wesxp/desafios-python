sexo = str(input('Digite  o seu sexo M ou F :')).upper()

while sexo  not in 'MmFf':
    sexo = str(input(' Você não Digitou uma das opções M ou F:'))
print(f'O sexo digitado foi {sexo},Obrigado!!')