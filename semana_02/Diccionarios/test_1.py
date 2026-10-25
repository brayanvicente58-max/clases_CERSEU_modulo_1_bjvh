# Creamos un diccionario con información de un estudiante
# Los diccionarios almacenan información en pares clave: valor

estudiante = {
    "nombre": "Lucía",
    "edad": 21,
    "carrera": "Ingeniería de Software",
    "promedio": 15.5
}

# Accedemos al nombre utilizando la clave "nombre"
print("Nombre:", estudiante["nombre"])

# Accedemos a la carrera utilizando su clave
print("Carrera:", estudiante["carrera"])

# Actualizamos el valor de la clave "promedio"
estudiante["promedio"] = 17.0

# Mostramos el promedio actualizado
print("Promedio actualizado:", estudiante["promedio"])

# Mostramos todas las claves del diccionario
print("Claves:", estudiante.keys())

# Mostramos todos los valores del diccionario
print("Valores:", estudiante.values())