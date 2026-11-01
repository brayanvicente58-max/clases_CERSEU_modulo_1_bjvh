#Creamos el diccionario del estudiante
estudiante = {
    "nombre": "Carlos",
    "edad": 20,
    "carrera": "Ingeniería de Software",
    "promedio": 15
}

#Consultamos los valores utilizando sus claves
print("Nombre: {}".format(estudiante["nombre"]))
print("Carrera: {}".format(estudiante["carrera"]))

# Modificamos el promedio directamente
estudiante["promedio"] = 18

#Agregamos una nueva clave
estudiante["ciclo"] = 4

#Verificamos si existe una clave en el dicionario
if "correo" in estudiante:
    print("El correo está registrado")
else:
    print("El correo no está registrado")

#Mostramos el diccionario actualizado
print("\nEstudiante actualizado:")
print(estudiante)