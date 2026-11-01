"""Listas en Python"""
"""
Listas: caso de actualizacion de notas
"""

notas = [12, 18, 16, 20, 11, 14, 13]

i = 0

for nota in notas:
    print(notas[i])
    notas[i] = nota - 2
    print("nota actualizada: {}".format(notas[i]))
    i += 1
#La nueva lista actualizada tendrá la mitad del valor de cada nota
#Agregar dos notas en la lista que sean mayores a la las notas de la lista actualizada
print("---ACTUALIZACION DE NOTAS---")
a = 0
for nota_actualizada in notas:
    print(notas[a])
    notas[a] = nota_actualizada / 2
    print("nota calculada: {}".format(notas[a]))
    a += 1
print("notas actualizadas: {}".format(notas))
notas.append(15)
notas.append(17)
print("notas agragadas: {}, {}".format(notas[7], notas[8]))
print("notas actualizadas: {}".format(notas))