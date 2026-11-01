"""Funciones"""

var_1 = 100
var_2 = 80

"""
input: dos variables que pasarán por parámetro de la función
a, b: parámetros de la función 'sumar'
"""

def sumar(a, b):
    return a + b

resultado = sumar(var_1, var_2)
"""output: Lo que retorna la función"""

print(resultado)

resultado_2 = sumar(90.3, 400)
print(resultado_2)

resultado_3 = sumar(var_1, 590)
print(resultado_3)