
while True:
    print('=' * 30)
    n=int(input('Qual tabuada Você deseja: '))
    if n  <0:
        break
    for tabuada in range (1,11):
        res = n*tabuada
        print(f'{tabuada}x{n} = {res}')

print('Fim')

