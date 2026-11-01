"""Inputs y Outputs"""

usuario = input("Ingresa tu usuario: ")
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Su usuario es: {}".format(usuario))
print("Bienvenido/a {}".format(nombre))

actualizar = int(edad) + 5
print("La edad actualizada es: {}".format(actualizar))