numeros = ('ZERO','UM','DOIS','TRÊS', 'CINCO','SEIS', 'SETE','OITO','NOVE','DEZ')



while True:
    escolha = int(input('Digite um numero de 0 a 10:'))
    if 0 <=  escolha <=20:
        break
    print('Tente novamente!!')

print(f'O numero que você digitou foi {numeros[escolha]}')