

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


carro_1 = Carro("blanco", 55)
print("El color de carro 1: {}".format(carro_1.color))

carro_2 = Carro("negro", 65)
carro_2.marchas = 30000

print("Marchas totales del carro 2: {}".format(carro_2.marchas))

"""importante"""
"""No es posible llamar un atributo de datos que se le ha asignado a otra instancia de la clase"""
#print(carro_1.marchas)