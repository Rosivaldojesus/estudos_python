"""
As 4 caracteristicas da POO
Polimorfismo
Herança
Abstração
Encapsulamento
"""

class Carro:
    def __init__(self, motor, direcao, eletrico):
        self.motor = motor
        self.direcao = direcao
        self.eletrico = eletrico


    def partida(self):
        print("Dando partida no carro")


    def acelera(self):
        print("Carro acelerando e em movimento")

    def parar(self):
        print("Carro parado")


carro = Carro(1.8, "Hidraúlica", "Manual")

carro.partida()