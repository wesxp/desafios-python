vlrc = float(input('Qual é o valor da casa?R$'))

salario = float(input('Qual é o  seu salário?R$'))

anos = int(input('Em quantos anos você vai pagar a casa:'))

prestacao = vlrc/(anos * 12)

print(f'O valor das prestações é R${prestacao}')
if prestacao <= salario+(salario*30/100):
    print('Emprestimo aceito')
elif prestacao > salario+(salario*30/100):
    print('Emprestimo negado')

