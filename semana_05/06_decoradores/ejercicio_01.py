"""
Decoradores en Python
"""

"""Creación interna de la función decorativa"""

def funcionDecora(funcionB):
    def funcionC():
        print("1. Antes de ejecutar la función a decorar")
        funcionB()
        print("2. Después de ejecutar la función a decorar")
    return funcionC()


@funcionDecora
def saludo():
    print("Hola Pythonistas")

#rint(saludo())