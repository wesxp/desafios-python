num =int(input('Digite um numero:'))
tot = 0


for c in range(1,num+1):
    if num % c == 0:
        print('\033[34m',end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(c,end='')
print(f'\033[m Numero {num} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é PRIMO')
else:
    print('E por isso é NÃO É PRIMO')