print('Calculando a PA')
print('==++=='*20)
n = int(input('Digite o primeiro termo:'))
r = (int(input('Digite a razão da PA:')))

c = 1

while c <= 10:
 print(f'{n}➔',end=' ')
 n += r
 c+=1
print('FIM', end=' ')