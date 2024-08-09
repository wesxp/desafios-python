import random


print('=='*13)
print('|JOGO DO PAR OU IMPAR|')
print('=='*13)

v ='Ganhou'
d = True
cont = 0
while d :
    pc = random.randint(1,100)
    numero = int(input('Digite um numero :'))
    escolha = str(input('Faça sua jogada| PAR ou IMPAR :')).upper()
    n = pc + numero
    resposta = n % 2
    print(f'O numero que o computador jogou foi {pc}')
    if resposta == 1 and escolha =='PAR':
        print('Você perdeu')
        d = False
    elif resposta == 1 and escolha == 'IMPAR':
        print('Você Venceu!!')
    elif resposta == 0  and escolha == 'PAR':
        print('Você Venceu!!')
    elif resposta == 0 and escolha == 'IMPAR':
        print('Você perdeu')
        d = False
    cont += 1
print(f'Você fez um total de {cont} jogadas')