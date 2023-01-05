soma = 0
count = 0
media = 0
for i in range(13,74):
    if(i % 2 == 0):
        count += 1
        soma += i
        media = soma / count

print(f'A média dos pares é: {media}')
