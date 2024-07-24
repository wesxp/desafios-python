import random
from time import sleep
lista = ('Pedra','Papel','Tesoura')
computador = random.randint(1,3)
print('Escolha uma opção de jogada:'
      '\n[1]Pedra'
      '\n[2]Papel'
      '\n[3]Tesoura')
escolha = int(input('Qual opção você escolheu :'))
print('JO')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')

print('-=' *11)
print(f'O computador jogou {lista[computador]}')
print(f'O jogador jogou {lista[escolha]}')
print('-=' *11)
print('Vencededor:')

if computador == 1:
   if escolha == 1:
         print('Empate')
   elif escolha == 2:
         print('Jogador Ganhou')
   elif escolha == 3:
         print('Computador Ganha')
   else:
         print('Jogada Invalida')

if computador == 2:
    if escolha == 1:
        print('Computador Ganha')
    elif escolha == 2:
        print('empate')
    elif escolha == 3:
        print('Jogador Ganhou')
    else:
        print('Jogada Invalida')

if computador ==3:
    if escolha == 1:
        print('Jogador Ganhou')
    elif escolha == 2:
        print('Computador ganhou')
    elif escolha == 3:
        print('Empate')
    else:
        print('Jogada Invalida')
