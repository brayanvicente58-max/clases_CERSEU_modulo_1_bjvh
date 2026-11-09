"""
Decoradores en Python
"""
"""Uso de los *args, **kwards"""

def funcionDecoradora(funcion):
    def funcionC(*args, **kwargs):
        print("1. Antes de ejecutar la función a decorar")
        resultado = funcion(*args, **kwargs)
        print(*args)
        print("Uso de los valores de los valores *args")
        for dato in args:
            print(dato)
        print("Uso de los valores de **kwards")
        for key, value in kwargs.items():
            print("{} = {}".format(key, value))
        print("2. Después de ejecutar la función decorada")
        return resultado
    return funcionC


@funcionDecoradora
def saludar(nombre, apellido, edad, **kwargs):
    print("Hola {} {}, usted tiene {} años".format(nombre, apellido, edad))
    for key, value in kwargs.items():
        print("{} = {}".format(key, value))

saludar("Julio", "Gutierrez", 34, ciudad_1="Lima", ciudad_2="Arequipa", ciudad_3="Cusco")