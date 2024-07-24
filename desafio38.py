n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))

if n1 == n2:
    print('Os numeros são iguais ')
elif n1 > n2:
    print(f'O numero \033[1:31m {n1} \033[1:37m é maior que {n2}')
else:
    print(f'O numero \033[1:31m{n2} \033[1:37m é maior que {n1}')