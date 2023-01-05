class Triangulo():

    # def setLadoA(self,a):
    #     self.ladoA = a

    def __init__(self,a,b,c):
         self.ladoA = a
         self.ladoB = b
         self.ladoC = c

    def calcularPerimetro(self):
        return f'O perímetro é: {self.ladoA + self.ladoB + self.ladoC}'


    def maiorLado(self):
        if(self.ladoA > self.ladoB and self.ladoA > self.ladoC):
           return (f'O maior lado é o lado A, com {self.ladoA}')
        elif(self.ladoB > self.ladoA and self.ladoB > self.ladoC):
            return (f'O maior lado é o lado B, com {self.ladoB}')
        elif(self.ladoC > self.ladoA and self.ladoC > self.ladoB):
            return (f'O maior lado é o lado C, com {self.ladoC}')
        else:
            return "Os lados são iguais!!!"
    
varavel = Triangulo(3,4,5)

print(varavel.maiorLado())

