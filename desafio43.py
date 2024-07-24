peso = float(input('Qual é o seu peso (kg):'))
altura = float(input('Qual é a sua altura (m)'))
imc = peso/(altura**2)
print(f'O seu imc é :{imc:.2f} ')

if imc < 18.5:
    print('Você está abaixo do peso normal')
elif imc >=18.5 and imc <25:
    print('Você está  no peso ideal')
elif imc >=25 and imc <30:
    print('Você está com sobrepeso')
elif imc >=30 and imc <40:
    print('Você está em estado de Obsidade')
elif imc>40:
    print('Você está estado de Obsidade mórbida ')