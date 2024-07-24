nota1 = float(input('Digite a primeira nota:'))

nota2 = float(input('Digite a segunda nota:'))

nota3 = float(input('Digite a primeira nota:'))

media = (nota3+nota1+nota2)/3

print(f'Sua média foil {media}\n'
      f'Então:')

if media < 5 :
    print('Você foi reprovado')
elif media >=5 and media <= 6.5:
    print('Você esta de recuperação')
else:
    print('Parabéns você foi aprovado(a)!!')
