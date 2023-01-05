import numpy as np

arr = np.random.rand(10)

arr

#mensagem = instrução
#somar

msg = str(input("Digite uma instrução: "))


def instrucao(msg):
    if(msg == "somar" or msg == "soma"):
        vals = int(input("digite os valores: "))
        valores = list(str(vals))
        soma = 0

        for i in range(0,len(valores)):
            if(valores[i].isdigit()):
                soma += int(valores[i])
            else:
                soma = soma
        return print(f'O resultado da soma é: {soma}')
    else:
        return "instrução inválida!"


instrucao(msg)