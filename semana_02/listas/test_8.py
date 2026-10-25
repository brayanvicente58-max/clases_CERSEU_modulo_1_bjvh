"""
Listas en Python

reverse(): Revierte el orden de la lista

"""
persona = ["Susana", "Gutierrez", 35, "20/07/1990"]

print("Los valores de mi lista: {}".format(persona))

persona.reverse()
print("Los valores de mi lista: {}".format(persona))

#Los cambios se mantienen sobre la lista
print(persona)