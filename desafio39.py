from datetime import date
ano = int(input('Digiteo ano que você  nasceu:'))
idade = date.today().year - ano
fez = ano + 18
falta_idade = 18 - idade

passou_idade = date.today().year - fez
print(f'Você tem {idade} anos ')
if idade < 18:
    print('Você   ainda não precisa se alistar para o exército\n'
          f'Mas falta {falta_idade} anos para se alistar!!')
elif idade == 18:
    print('Você precisa se alistar para o exército')
else:
    print(f'Passou a data de se alistar para o exército {passou_idade} anos atrás')
