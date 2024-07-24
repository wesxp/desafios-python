vlr1=int(input('Digite o primeiro valor:'))
vlr2=int(input('Digite o segundo valor:'))
vlr3=int(input('Digite o primeiro valor:'))

if vlr1 >vlr2 and vlr1>vlr3:
    print(f'O numero maior é {vlr1}')
if vlr2 > vlr1 and vlr2 > vlr3:
    print(f'O numero maior é {vlr2}')
if vlr3 > vlr1 and vlr3 > vlr2:
    print(f'O numero maior é {vlr3}')
if vlr1 < vlr2 and vlr1 < vlr3:
    print(f'O numero menor é {vlr1}')
if vlr2 < vlr1 and vlr2 < vlr3:
    print(f'O numero menor é {vlr2}')
if vlr3 < vlr1 and vlr3 < vlr2:
    print(f'O numero menor é {vlr3}')