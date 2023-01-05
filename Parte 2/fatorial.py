##FATORIAL DE QUALQUER NÚMERO
num = int(input("Digite um número: "))

for i in range(1,num):
    num *= i
    ##print(num)

print(f'O fatorial é: {num}')