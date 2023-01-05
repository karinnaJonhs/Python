#3. Peça ao utilizador que escreva 10 palavras; e guardar as palavras numa lista. Depois de todas as palavras guardadas, escreva no ecrã todos os elementos da lista que comecem com o caractere "a".

##crio um array para colocar as palavras
palavras = []

##Array para palavras que comecem com A
comA = []

##faço um for para pedir ao usuario 10 palavras, sendo que, se alguma se iniciar com a, adicionarei a mesma ao array "comA"
for i in range (0,10):
    word = input("Digite a palavra: ")
    if(word[0] == "a"):
        comA.append(word)

##retorno o array
print(comA)


