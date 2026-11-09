
"""
Programación Orientada a Objetos (POO)
Tema: Polimorfismo
"""

class Perro:
    def sonido(self):
        print("El perro dice: Guauuuu")


class Gato:
    def sonido(self):
        print("El gato dice: Miauuu")


class Vaca:
    def sonido(self):
        print("La vaca dice: Muuuu")


#Función que aplica polimorfismo
def emitir_sonidos(animales):
    for animal in animales:
        animal.sonido()

#Instanciar las clases
perro = Perro()
gato = Gato()
vaca = Vaca()

#Lista de diferentes objetos
lista_animales = [perro, gato, vaca]

#Ejecutar la función
print("SONIDOS DE LOS ANIMALES")
emitir_sonidos(lista_animales)
