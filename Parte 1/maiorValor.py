num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = num1

lista = list((num1,num2,num3))

for i in range(0,3):
    if(lista[i] > maior):
        maior = lista[i]

print(f'O maior número é o: {maior}')