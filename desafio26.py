frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A aparece {frase.count('A')} vezes na frase  ')
print(f'A primeira letra A apareceu na posição {frase.find('A')+1}')
print(f'Onde aparece a ultima ocorrencia de A{frase.rfind ('A')+1}')