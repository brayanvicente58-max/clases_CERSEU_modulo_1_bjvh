
"""
Listas en Python

Listas,
len(): Obtener el tamaño de la lista
append(): Agregar elementos en la lista

"""
paises = [] #inicio una lista vacía
print("Mi lista de países, contiene los valores: {}".format(paises))
print(len(paises))

print("_________________________________________")

"""Agregar datos a la lista"""
paises.append("Perú")
paises.append("España")
paises.append("Argentina")

print("Mi lista de paises, contiene los valores: {}".format(paises))

paises.append("Colombia")
print("Mi lista de países: {}".format(paises))

print("_________________________________________")
pais = paises[0]
print("El primero valor, elemento(0), de mi lista es: {}".format(pais))

#Importante:
#El valor dentro de una lista lo obtenemos mediante su índice
#Siempre el primer valor empieza en índice 0

pais_2 = paises[1]
print(pais_2)

pais_3 = paises[-2]
print(pais_3)
