##51 a 60 = 50€
##61 a 80 = 100€
##acima de 80 = 200€

vel = int(input("Velocidade Máxima: "))

if(vel <= 50):
    print("Suave")
elif(vel > 50 and vel <= 60):
    print("Segura aí a multa de 50€!")
elif(vel > 60 and vel <= 80):
    print("Segura aí a multa de 100€!")
else:
    print("Segura aí a multa de 20s0€!")