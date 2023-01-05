
##Um programa que faça a escada sequencial

num = int(input("Digite um número: "))

def escadaSequencial(num):
    sequencia = []
    for i in range(1,num+1):
        sequencia.append(str(i))
    print(sequencia)
    
    linha = []
    for j in range(1,len(sequencia)+1):
        linha.append(sequencia[j-1])
        lin = " ".join(linha)
        print(lin)

escadaSequencial(num)



