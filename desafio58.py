import random
n = random.randint(1,10)
tentativa = int(input('Digite um  numero que o computador esta pensando:'))
c = 0
while tentativa != n:
    tentativa = int(input('Você não acertou tente novamente:'))
    c += 1
print(f'Parabéns você conseguiu , o valor que o computador pensou foi {tentativa}!!')

print(f'Você tentou {c} vezes para chegar no resultado.')