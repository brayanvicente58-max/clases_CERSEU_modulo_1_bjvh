"""Uso de cond. if"""

edad_1 = int(input("Ingrese la primera edad: "))
edad_2 = int(input("Ingrese la segundad edad: "))

if edad_1 > edad_2:
    print("La primera edad es mayor a la segunda")
elif edad_1 == edad_2:
    print("Las edades ingresadas son iguales")
    edad_2 = edad_2 + 5
    print("La segunda edad actualizada es: {}".format(edad_2))
else:
    print("La segunda edad es mayor que la primera edad")