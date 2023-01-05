def soma_elementos_tuplo(tuplo):
    soma = 0
    for i in range(0,len(tuplo)):
         soma += int(tuplo[i])
    return soma


def soma_elementos_tuplo(tuplo):
    soma = sum(tuplo)
    print(soma)

## Considere a função find_codons(dna) que recebe uma string dna e imprime no ecrã todos os codões identificados nessa string. Preencha as linhas de código em falta, escrevendo o código todo na caixa abaixo, na função find_codons, de modo a que esta proceda de acordo com o exemplo:
>>> find_codons( “ATGTTCGGT” )


[“ATG”, “TTC”, “GGT”]

def find_codons(dna):
    codons_lst = []
    for i in range(0, len(dna) , 3):
        codon = dna[i:i+3]
        codons_lst.append(codon)
    return codons_lst