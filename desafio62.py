print('Calculando a PA')
print('==++=='*20)
n = int(input('Digite o primeiro termo:'))
r = (int(input('Digite a razão da PA:')))
total = 0
mais = 10

c = 1
while mais != 0:
  total = total + mais
  while c <= total:

    print(f'{n}➔',end=' ')
    n += r
    c+=1
  print('Pausa')

  mais =int(input('Quantos termos você quer a mais :'))
print('FIM')