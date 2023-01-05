#Escrevaum programaemPython que recebaumastring do user e mostrede tráspara frente.

nome = str(input("Digite um nome: "))
name = list(nome)
name.reverse()

print("".join(name))