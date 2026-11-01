"""
Programación orientada a objetos
"""

class Carro:
    """atributos"""
    ruedas = 4
    """Constructor: Valores que van a tener por defecto mi clase que se isntanacia en una variable"""
    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

    """Métodos: Son las funciones de las clases"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frenar(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

carro_1 = Carro("rojo", 15)
print("Color carro 1: {}".format(carro_1.color))
print("Aceleración: {}".format(carro_1.aceleracion))
print("La cantidad de ruedas de carro 1: {}".format(carro_1.ruedas))

carro_2 = Carro("azul", 40)
print("Color carro 2: {}".format(carro_2.color))
print("Aceleración: {}".format(carro_2.aceleracion))
print("La cantidad de ruedas de carro 2: {}".format(carro_2.ruedas))