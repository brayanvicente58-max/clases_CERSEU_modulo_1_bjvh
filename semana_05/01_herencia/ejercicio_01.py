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


class CarroVolador(Carro):
    ruedas = 6

    def __init__(self, color, aceleracion, estado_volando):
        super().__init__(color, aceleracion)
        self.estado_volando = estado_volando

    def vuela(self):
        if not self.estado_volando:
            self.estado_volando = True
            print("El carro ha comenzado a volar.")
        else:
            print("El carro ya está volando.")

    def aterriza(self):
        if self.estado_volando:
            self.estado_volando = False
            print("El carro ha aterrizado.")
        else:
            print("El carro ya se encuentra en tierra.")

#Creación de objetos
carro_1 = Carro("Negro", 69)
carro_volador = CarroVolador("Blanco", 35, False)

#Información inicial del carro volador
print("===== INFORMACIÓN INICIAL =====")
print("Color del carro volador: {}".format(carro_volador.color))
print("Aceleración: {}".format(carro_volador.aceleracion))
print("Cantidad de ruedas: {}".format(carro_volador.ruedas))
print("Velocidad inicial: {}".format(carro_volador.velocidad))
print("¿Está volando?: {}".format(carro_volador.estado_volando))

#Métodos propios de la clase hija
print("\n===== MÉTODOS DE CARRO VOLADOR =====")
carro_volador.vuela()
print("¿Está volando?: {}".format(carro_volador.estado_volando))

#Métodos heredados de la clase padre
print("\n===== MÉTODOS HEREDADOS DE CARRO =====")
carro_volador.acelerar()
carro_volador.acelerar()
carro_volador.acelerar()

carro_volador.frenar()
carro_volador.frenar()

print(carro_volador.velocidad)

#Finalmente
print("\n===== ESTADO FINAL =====")
print("Velocidad actual: {}".format(carro_volador.velocidad))

carro_volador.aterriza()
print("¿Está volando?: {}".format(carro_volador.estado_volando))

#Demostración de la herencia
print("\n====== COMPROBACIÓN DE HERENCIA ======\n")

#La clase hija puede utilizar métodos de la clase padre
carro_volador.acelerar()

#La clase padre no hereda los métodos exclusivos de la hija
# carro_1.vuela()  # AttributeError