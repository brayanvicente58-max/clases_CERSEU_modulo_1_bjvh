"""
Ejercicio 03
Participación

Requisitos:
- Crear una función que multiplicará 4 valores (int y floats)
- La función tendrá un parámetro que contendrá un valor por defecto
- Mostrar 2 casos donde se ingresó los valores donde uno no afectará el valor del parámetro
que ya contiene un valor y otro donde si lo estará afectando
- Ingresar los valores por consola

"""

def multiplicar(a, b, c, d = 1):
    return a * b * c * d
print("=== CASO 1: No se ingresa el 4to valor (usa el valor por defecto) ===")
v1 = int(input("Ingrese el primer valor: "))
v2 = int(input("Ingrese el segundo valor: "))
v3 = int(input("Ingrese el tercer valor: "))
resultado_1 = multiplicar(v1, v2, v3)
print("El resultado de la multiplicación es: "f"{resultado_1}\n")
print("=== CASO 2: Sí se ingresa el 4to valor (afecta y modifica el resultado) ===")
w1 = int(input("Ingrese el primer valor: "))
w2 = int(input("Ingrese el segundo valor: "))
w3 = int(input("Ingrese el tercer valor: "))
w4 = int(input("Ingrese el cuarto valor (modifica el valor por defecto): "))

resultado_2 = multiplicar(w1, w2, w3, w4)
print("El resultado de la multiplicación es: "f"{resultado_2}")