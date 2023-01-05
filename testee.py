lista = input("digite números: ")
li = list(lista)
teste = {}
for i in range(0,len(li)):
    teste.append(int(li[i]))

print(teste)
for i in range(0,len(teste)):
    print(f"O numero {teste[i]} está na posição {teste.index(teste[i])}")