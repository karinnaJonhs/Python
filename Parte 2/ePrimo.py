num = int(input("Digite um número: "))

soma = 0
for i in range(2,num):
    if(num % i != 0 and num % num == 0):
        soma += 0
    else:
        soma += 1

if(soma == 0):
    print("É PRIMO!")
else:
    print("Não é primo!")