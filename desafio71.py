print('='*10)
print('|BANCO WOS|')
print('='*10)

vlr =float(input('Que valor vocÇe quer sacar? R$:'))
total = vlr
ced = 50
totced = 0
while  True:
    if total >=ced:
        total -=ced
        totced +=1
    else:
        print(f'Total de {totced} cédulas de {ced}')
        if ced ==50:
            ced = 20
        elif ced ==20:
            ced =10
        elif ced ==10:
            ced =1
        if total == 0:
            break
