
s = cont = 0
while True:
    n = int(input('Digite um numero(Digite 999 para encerrar):'))
    if n ==999:
        break
    s+=n
    cont+=1
print(f' você digitou {cont} vezes e a soma dos '
      f'valores digitados é de {s} ')

print('Fim')