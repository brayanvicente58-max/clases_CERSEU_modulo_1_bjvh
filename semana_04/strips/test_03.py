"""Usando las propiedades de las cadenas o strings"""

"""Métodos de strings"""

cadena = "Conexión a BD con Python"

cadena_2 = cadena.replace(cadena[0:8], "Nueva conexión")
print("Cadena actualizada: {}".format(cadena_2))

"""Eliminación de espacio en blanco"""
cadena_3 = "Conexión a BD con Python         "
cadena_4 = cadena_3.rstrip()

print(cadena_3)
print("Actualización de cadena: {}".format(cadena_4))

cadena_5 = "       Conexión a BD con Python"
cadena_6 = cadena_5.lstrip()

print(cadena_5)
print("Actualización de cadena: {}".format(cadena_6))