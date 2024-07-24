salario = float(input('Digite o valor do Salário do funcionário: R$'))

if salario <=1250:
    novo = salario+ (salario*15/100)
    print(f"O novo sálario é de R${novo}")
else:
    novo = salario+(salario*10/100)
    print(f"O novo sálario é de R${novo}")
