"""
Listas en Python

del: Eliminar un valor indicando el índice de la lista

"""

paises = []
paises.append("Perú")
paises.append("Brasil")

#2da forma para agregar elementos a una lista (más reducido)
paises.extend(["Colombia", "México", "Canandá", "Alemania", "Francia"])

print(paises)

del paises[2]
print(paises)

del paises[4]
print(paises)