

num = int(input("Digite um número: "))

##Um Programa que imprima aquela escadinha lá de números
def escada(numero):   
     for num in range(1, numero+1):       
              linha = ""       
              for i in range(0, num):           
                     linha += str(num) + ' '       
              print(linha)


escada(num)

