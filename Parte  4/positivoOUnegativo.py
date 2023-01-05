##se for positivo, retornar: P; se for negativo: N

num = input("Digite um número: ") 

def validar(num):
    if num.isdigit():
        if(num > 0):
            return "P"
        else:
            return "N"
    else:
        return "Argumento Inválido!"

print(validar(num))