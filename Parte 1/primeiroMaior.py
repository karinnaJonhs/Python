#Verificar se o primeiro número eh mairo que a soma dos outros dois!#

primeiro = int(input("Primeiro número: "))
segundo = int(input("Segundo número: "))
terceiro = int(input("Terceiro número: "))

soma = segundo + terceiro

if(primeiro < soma):
    print("O primeiro é MENOR que a soma dos outros dois!")
else:
    print("O primeiro é MAIOR que a soma dos outros dois! ")
