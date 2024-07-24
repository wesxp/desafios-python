total =0
cont = 0
for c in range(1,500):
    div = c%3
    if div == 0:
        cont += 1
        print(c)
    total += c
print(f'A dos  {cont} numeros é {total}')
print('Fim')