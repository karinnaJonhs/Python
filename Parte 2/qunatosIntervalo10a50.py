#Ler10 valores, um de cadavez, e contarquantosdeles estãono intervalo[10,50] e quantosdeles estãofora desteintervalo, mostrandoestasinformações. 

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
num4 = int(input("Digite mais um número: "))
num5 = int(input("Digite mais um número: "))
num6 = int(input("Digite mais um número: "))
num7 = int(input("Digite mais um número: "))
num8 = int(input("Digite mais um número: "))
num9 = int(input("Digite mais um número: "))
num10 = int(input("Digite o último número: "))

lista = list((num1,num2,num3,num4,num5,num6,num7,num8,num9,num10))
print(lista)

count= 0

for i in range(0,10):
    if(lista[i] > 10 and lista[i] < 50):
        count += 1

print(f'A quantidade de números entre 10 e 50 é: {count}')