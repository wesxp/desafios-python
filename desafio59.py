n1 = int(input('Digite o primeiro valor:'))
n2 = int(input('Digite o Segundo valor:'))

escolha  = 0
while escolha != 5 :
    escolha = int(input('MENU'
                        '\n[1]somar'
                        '\n[2]multiplicar'
                        '\n[3]maior'
                        '\n[4]novos números'
                        '\n[5]sair do programa '
                        '\nEscolha uma opção de :'))
    if escolha == 1:
        m = n1+n2
        print(f'O valor da soma  de {n1}+{n2} é {m}')
    elif escolha == 2:
        mul = n1*n2
        print(f' O valor da multiplicação é  {mul}')
    elif escolha == 3:
        if n1 > n2 :
            print(n1)
        else:
            print(n2)
    elif escolha == 4:
        n1 = int(input('Digite o numero novo:'))
        n2 = int(input('Digite o segundo numero:'))
    elif escolha != 5 :
        print('Você digitou uma opção invalida tente novamente')
print('Finalizando ')