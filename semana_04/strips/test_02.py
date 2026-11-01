"""Usando las propiedades de las cadenas o strings"""

"""Concatenación"""

nombre = input("Nombre: ")
apellido = input("Apellido: ")

nombre_completo = nombre + " " + apellido
print("Nombre completo de usuario: {}".format(nombre_completo))

print("Nombre completo del usuario: {} {}".format(nombre, apellido))