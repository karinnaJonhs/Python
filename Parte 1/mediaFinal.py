primeiro = int(input("Primeira nota: "))
segundo = int(input("Segunda nota: "))
terceiro = int(input("Terceira nota: "))

media = (primeiro+segundo+terceiro)/3

if(media >= 13):
    print("APROVADO UHUUU")
elif(media < 13 and media >= 9):
    print("MÉDIA! Ufa! Passou!")
else:
    print("Bombou. :C")