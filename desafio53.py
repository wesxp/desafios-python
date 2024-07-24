frase =str(input('Digite uma frase: ')).strip().upper()

palavra = frase.split()
junto ='*'.join(palavra)
inverso =''
print(f'Você digitou a frase {palavra}')

for letra in range(len(junto)-1,-1,-1):
    inverso+= junto[letra]
print(inverso)

