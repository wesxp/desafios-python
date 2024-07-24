cont = 0
cont1 = 0
from datetime import date
for n in range(1,8):
    data = int(input('Digite o  ano você nasceu:'))
    maioridade =  date.today().year - data
    if maioridade >=21:

     cont += 1
    elif maioridade < 21:
        cont1 +=1
print(f'Das 7 pessoas {cont} é maior de idade ')
print(f'Das 7 pessoas {cont1} é menor de idade ')


