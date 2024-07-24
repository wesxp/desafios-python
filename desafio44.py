print('==============LOJAS WES================')
compras =float(input('Qual foi o  valor das compras R$ : '))

total = compras - (compras*10/100)
total1 = compras - (compras*5/100)
total2 = compras / 2
print('Qual a forma de pagamento :'
      '\n [1] à vista  dinheiro/cheque'''
      '\n [2] à vista cartão'
      '\n [3] 2x no cartão'
      '\n [4] 3x ou mais no cartão')

pag = int(input('Qual opção:'))

if pag == 1:
      print(f'O valor das compras ficará R$ {total}')
elif pag == 2:
      print(f'O valor das compras ficará R${total1}')
elif pag == 3:
      print(f'O valor das compras ficará  2x de R$ {total2}')
elif pag ==4:
      total3 = compras + (compras*20/100)
      parcelas = int(input('Qunatas parcelas?:'))
      totpreco = total3 / parcelas
      print(f'O valor total ficará {parcelas}X de R${totpreco}')
else:
      print('Opção invalida :\033[1:31m tente novamente :\033[1m !!')
