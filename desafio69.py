print('='*20)
print('|CADASTRE UMA PESSOA|')
print('='*20)
cont = cont1  = cont2 = 0
while True:
    idade = int(input("idade: "))
    sexo = str(input("sexo: ")).upper()
    resposta = str(input('Quer continuar? S/N: ')).upper()
    if idade >= 18:
        cont +=1
    if idade <=20 and sexo == 'F':
        cont2 +=1
    if sexo == 'M':
        cont1 += 1

    if resposta == 'N':
        break

print(f'Total de pessoa com idade maior de 18 anos é  {cont}')
print(f'Temos um total de {cont1} homens')
print(f'E temos {cont2} mulheres com idade  menor que 20 anos ')
