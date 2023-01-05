#Crieum programaque solicitea password de um user e depois, peçapradigitarnovamenteatéque as duassenhassejamcorrespondentes.

passw = str(input("Digite sua senha: "))
conf = ""

while passw != conf:
    conf = input("Digite a senha novamente: ")

print("BINGO!")

