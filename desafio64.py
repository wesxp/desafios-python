n = int(input('Digite um valor (digite 999 para parar):'))

cont = 0
soma = 0
while  n !=  999:
    soma += n
    cont += 1
    n = int(input('Digite um valor (digite 999 para parar):'))
print(f'A soma dos valores é {soma}')
print(f'Você digitou {cont} numeros')
print('Fim')
