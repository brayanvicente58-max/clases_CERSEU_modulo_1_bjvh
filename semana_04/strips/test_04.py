
"""Usando las propiedades de las cadenas o strings"""
"""Métodos de strings"""
"""Separación de string: split()"""

cadena = "Python para la predicción de fraudes bancarios"

cadena_sin_espacios = cadena.split()

print(cadena_sin_espacios)

pabra_coincidencia = input("Ingrese la palabra a buscar: ")

if pabra_coincidencia in cadena_sin_espacios:
    print("Si hay coincidencia")
else:
    print("No existe coincidencia")

#for palabra in cadena_sin_espacios:
#    if palabra == pabra_coincidencia:
#        print("Si existe la palabra '{}' dentro de la cadena".format(palabra))
#    else:
#        print("No existe coincidencia")

cadena_sep_coincidencia = cadena.split(sep="de")
print(cadena_sep_coincidencia)

for palaraba in cadena_sep_coincidencia:
    print(palaraba)