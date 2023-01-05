##Calcular sálario
##Abaixo de 500, aumentar 15%
##Entre 500 e 1500, aumentar 10%
##Acima de 1500, aumentar 5%

salario = float(input("Digite seu salário: "))

if salario < 500:
    salario *= 1.15
    print(f'O novo valor é: {salario}')
elif salario >= 500 and salario <= 1500:
    salario *= 1.10
    print(f'O novo valor é: {salario}')
else:
    salario *= 1.05
    print(f'O novo valor é: {salario}')