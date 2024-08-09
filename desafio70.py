print('='*15)
print('|LOJÃO DO BRÁS|')
print('='*15)
barato =''
valor = cont = menorpreco = totmil =  0
while True:
    produto = str(input('Digite o nome do produto:'))
    preco = float(input('Digite o preço: R$'))
    p = str(input('Quer continuar? S/N')).upper()
    cont+=1
    valor+=preco
    if cont == 1:
        menorpreco= preco
        barato = produto
    else:
        if valor < menorpreco:
            menorpreco = preco
            barato = produto
    if  preco > 1000:
        totmil += 1
    if p == 'N':
        break
print("=======FIM DO PROGRAMA=====")
print(f'O total de compra foi de R${valor}')
print(f'Temos {totmil} produto custando mais de R$1000.00')
print(f'O produto mais barato  foi {barato} que custa {menorpreco}')