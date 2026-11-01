"""Intervención"""

"""
Requisitos:
- Crear una lista de notas, 10 notas
- Obtener la suma de notas, utilizando el recorrido, apoyarse de una variable auxiliar
- Obtener las notas aprobadas y desaprobadas, empezar con listas vacías
- Obtener el promedio de notas, dentro de una variable
- Mostrar la nota más baja y la más alta

"""
notas = [11, 12, 6, 7, 13, 14, 15, 10, 9, 4]
i = 0
aprobados = []
desaprobados =[]
for nota in notas:
    i += nota
    if nota >= 11:
        aprobados.append(nota)
    else:
        desaprobados.append(nota)

promedio = i / len(notas)
min_nota = min(notas)
max_nota = max(notas)
print("Lista de notas: "f"{notas}")
print("Suma total de notas: "f"{i}")
print("Notas aprobadas: "f"{aprobados}")
print("Notas desaprobadas: "f"{desaprobados}")
print("Promedio de notas: "f"{promedio:.2f}")
print("Nota más baja: "f"{min_nota}")
print("Nota más alta: "f"{max_nota}")