num = int(input('Digite um numero inteiro :'))
print('Escolha uma das opções de conversão:'
      '\n[1]Converter para binário'
      '\n[2]Converter para Octal'
      '\n[3]Converter para Hexadecimal')
opcao = int(input('Digite uma opção:'))

if opcao == 1:
      print(f'Convertido para binário é {bin(num)}')
elif opcao == 2:
      print(f'Convertido para Octal é {oct(num)}')
elif opcao == 3:
      print(f'Convertido  para Hexadecimal é {hex(num)}')