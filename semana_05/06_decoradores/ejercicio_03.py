"""
Ejercicio 03 - Decoradores
Requisitos:

* Crear un decorador llamado validar_positivos que verifique que todos los argumentos numéricos de una función
sean mayores que 0.
* Si algún argumento no cumple la condición, debe lanzar un ValueError con el mensaje
"Todos los argumentos deberán ser positivos".
* Aplicar el decorador sobre una función calcular_promedio(*args) que
reciba una cantidad variable de números y retorne el promedio. Y mostrar también la cantidad de parámetros de
la función

Probar la función con 3 casos correctos y uno que lance la excepción

"""

def validar_positivos(func):

    def envoltura(*args, **kwargs):
        # Verificamos si alguno de los argumentos posicionales es menor o igual a 0
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Todos los argumentos deberán ser positivos")

        # Verificamos también en los argumentos con clave por si acaso
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value <= 0:
                raise ValueError("Todos los argumentos deberán ser positivos")

        # Si todo es correcto, ejecuta la función original
        return func(*args, **kwargs)

    return envoltura


# Aplicar el decorador sobre la función calcular_promedio
@validar_positivos
def calcular_promedio(*args):

    cantidad_parametros = len(args)
    print(f"Cantidad de parámetros recibidos: {cantidad_parametros}")

    if cantidad_parametros == 0:
        return 0.0

    promedio = sum(args) / cantidad_parametros
    return promedio


# Pruebas (3 casos correctos y 1 que lanza la excepción)

print("--- CASO 1: Tres números positivos ---")
try:
    resultado = calcular_promedio(12, 15, 18)
    print(f"El promedio es: {resultado:.2f}\n")
except ValueError as e:
    print(f"Error capturado: {e}\n")

print("--- CASO 2: Cuatro números positivos ---")
try:
    resultado = calcular_promedio(10, 20, 30, 40)
    print(f"El promedio es: {resultado:.2f}\n")
except ValueError as e:
    print(f"Error capturado: {e}\n")

print("--- CASO 3: Un solo número positivo ---")
try:
    resultado = calcular_promedio(14)
    print(f"El promedio es: {resultado:.2f}\n")
except ValueError as e:
    print(f"Error capturado: {e}\n")

print("--- CASO 4: Caso erróneo (incluye un número negativo o cero) ---")
try:
    # Esto lanzará la excepción ValueError requerida
    resultado = calcular_promedio(12, -5, 18)
    print(f"El promedio es: {resultado:.2f}\n")
except ValueError as e:
    print(f"Error capturado exitosamente: {e}\n")