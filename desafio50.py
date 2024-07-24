soma = 0
for c in range(1,7):
    num = int(input('Digite um  numero:'))
    par = num%2
    if par ==0:
        soma +=num
print(soma)
print('Fim')