from datetime import date
ano = int(input('Que ano vamos analisar:'))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and  ano % 100 != 0 or ano %400 ==0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'o ano {ano} Não é BISSEXTO')