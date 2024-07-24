import random
num = random.randint(1,10)
print('Pense em um numero de 0 a 10 ')
print('Pensou?')
numero =int(input('Digite  o numero que você pensou?:'))
if numero == num:
    print(f'O numero que o computador pensou foi {num} e você acertou')
else:
    print(f'O numero que o computador pensou foi {num} você errou!!!')

