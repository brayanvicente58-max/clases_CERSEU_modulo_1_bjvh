"""Manejo de errores"""
"""
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError

"""

"""
Estructura y uso

try:
    #camino exitoso
    bloque de código 1
except 'excepción #1'
    bloque de código 2
else:
    bloque de código 3
"""

def division(a, b):
    try:
        resultado = a / b
        print("División exitosa")
    except ZeroDivisionError:
        print("No es posible dividir estos valores, no es posible la división entre 0")
    else:
        print("Resultado: ", resultado)

division(1000, 2)
division(400, 0)
division(2, 500)