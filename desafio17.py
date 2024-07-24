import math
cateto1 = float(input('Digite o valor do cateto 1 : '))
cateto2 = float(input('Digite o valor do cateto 2 : '))

soma_cateto = (math.pow(cateto1,2)+ math.pow(cateto2, 2))

hipotenusa = math.sqrt(soma_cateto)

print(f'O valor da hipotenusa é de {math.floor(hipotenusa)}')

from math import hypot
cat1 = float(input('Digite o valor dq cateto1:'))
cat2 = float(input('Digite o valor dq cateto2:'))
hipotenusa1 = hypot(cat1,cat2)

print(f'O valor da hipotenusa é de {hipotenusa1}')