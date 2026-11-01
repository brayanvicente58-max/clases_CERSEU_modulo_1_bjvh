# Lista original de números
numeros = [12, 7, 25, 18, 30, 9, 14, 21, 6, 11]

# Listas para almacenar los resultados
pares = []
impares = []

# Acumulador para sumar los números pares
suma_pares = 0

# Recorrer la lista original
for numero in numeros:

    # Verificar si el número es par
    if numero % 2 == 0:
        pares.append(numero)
        suma_pares += numero
    else:
        impares.append(numero)

# Resultados
print("Lista original:", numeros)
print("Números pares:", pares)
print("Números impares:", impares)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))
print("Suma de pares:", suma_pares)