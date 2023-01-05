#Escrevaum programaemPython para encontrarnúmerosentre 100 e 400 (ambos inclusivé), ondecadadígitode um númeroéum númeropar. Osnúmerosobtidosdevemser impressosemsequênciaseparadapor vírgulas.

lista = []

for i in range(100,401):
    if(i % 2 == 0):
        lista.append(str(i))

print(",".join(lista))

