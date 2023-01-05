A = int(input("Digite o primeiro número: "))
B = int(input("Digite o segundo número: "))

maior = A

lista = list((A,B))

for i in range(1,2):
    if(lista[i] > maior):
        maior = lista[i]
        print(f'O maior número é o: {maior}')
    elif(lista[i] == maior):
        print("Números Iguais!")


