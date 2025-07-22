
#Crie uma classe carro, motor e fabricante e coloque nome
#Faça a ligação entre Carro e um Motor 
#obs: Um motor pode ser de vários carros
# faça a ligação entre carro e um fabricante
# obs: um fabricante pode fabricar vários carros
#exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome, Motor, Fabricante):
        self.nome = nome
        self.motor = Motor
        self.fabricante = Fabricante

class Motor:
    def __init__(self, nome):
        self.nome = nome

        
class Fabricante:
    def __init__(self, nome):
        self.nome = nome

Carro1 = Carro('Fusca', Motor('1.0'), Fabricante('Volkswagen'))
Carro2 = Carro('Civic', Motor('2.0'), Fabricante('Honda'))
print(f'Carro: {Carro1.nome}, Motor: {Carro1.motor.nome}, Fabricante: {Carro1.fabricante.nome}')
print(f'Carro: {Carro2.nome}, Motor: {Carro2.motor.nome}, Fabricante: {Carro2.fabricante.nome}')