from datetime import date

nome = str(input('Digite o nome do(a) atleta:'))
nascimento = int(input('Digite  a data de nascimento do atleta:'))


idade =  date.today().year - nascimento

print(f'A Categoria da(o) atleta {nome} é :')
if idade <= 9:
    print('Categoria Mirim')
elif idade > 9 and idade <= 14:
    print('Categoria infantil')
elif idade > 14 and  idade <=19:
    print('Categoria Junior')
elif idade == 20:
    print('Categoria Sênior')
else:
    print('Categoria Master')