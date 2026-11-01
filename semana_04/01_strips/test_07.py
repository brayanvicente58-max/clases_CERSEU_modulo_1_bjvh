"""
Intervención
"""

"""
Usando propiedades de string
Requisitos:
    - Ingresar su nombre y apellido por consola (variables distintas)
    - Obtener el tamaño de tu nombre completo y muéstralo en consola
    - Imprimir el resultado final, todo en mayúsculas: .upper()
    - Indicar mediante condicionales si el tamaño del nombre es mayor o no al apellido ingresado
    - Solamente ingresar el apellido paterno

"""
nombre = input("Ingresar su nombre: ")
apellido = input("Ingresar su apellido: ")
nombre_completo = nombre.upper() + " " + apellido.upper()
print("tamaño del nombre completo: {}".format(len(nombre_completo)))
print("nombre completo: {}".format(nombre_completo))
if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor al del apellido")
else:
    print("El tamaño del apellido es más grande que el tamaño del nombre")