"""Uso del búcle While"""

#numero = int(input("Ingrese un número de personas menores a 18: "))
conjunto_edad = [12, 14, 16, 20, 15]

i = 0
while len(conjunto_edad) < 30:
    #print(numero)
    if conjunto_edad[i] < 18:
        print("Cumple la edad de: ", conjunto_edad[i])
    else:
        print("Esta persona está fuera del conjunto")
        break # Rompe el búcle while
    #numero = numero + 1
    i = i + 1