sexo = str(input('Digite  qual é o seu sexo M/F:')).upper()

while sexo not in 'M F':
    sexo = str(input('Você Digitou errada , tente novamente (M/F)')).upper()
print(f'O sexo que você escolheu é {sexo}')