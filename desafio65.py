

resposta ='S'

soma = m = quant = 0



while resposta in 'Ss' :
    n = int(input('Digite um numero:'))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor  = n
    else:
        if n > maior :
            maior = n
        if n < menor :
            menor = n
    resposta = str(input('Quer continuar digite S/N : ')).upper()
m  = soma / quant
print(f'O menor numero foi {menor} e o maior {maior} ')
print(f'A média dos {quant} valores digitados é {m}')
print('Fim')