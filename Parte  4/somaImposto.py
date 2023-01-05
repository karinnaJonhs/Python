##A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

taxa = float(input("Digite a taxa de imposto (ex.: 1.50): "))

num = float(input("Digite o custo atual: "))

def somaImposto(taxaImposto, custo):
    return custo * taxaImposto;

print(somaImposto(taxa,num))


