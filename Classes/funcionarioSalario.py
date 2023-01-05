class Fucionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = float(salario)

    def setAumentarSalario(self,a):
        self.salario = self.salario * a
        return f'O novo salário é: {self.salario}€'


f = Fucionario("Augusto", 67)
print(f.setAumentarSalario(1.6))
