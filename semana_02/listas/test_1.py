# Creamos una lista que almacena cinco notas
notas = [14, 18, 12, 16, 20]

# Mostramos la primera nota
# En Python, el primer elemento tiene índice 0
print("Primera nota:", notas[0])

# Mostramos la última nota utilizando el índice -1
print("Última nota:", notas[-1])

# Obtenemos la nota más alta de la lista
print("Mayor nota:", max(notas))

# Obtenemos la nota más baja de la lista
print("Menor nota:", min(notas))

# Calculamos el promedio
# sum() suma todos los elementos de la lista
# len() devuelve la cantidad de elementos
promedio = sum(notas) / len(notas)

print("Promedio:", promedio)  # 16.0