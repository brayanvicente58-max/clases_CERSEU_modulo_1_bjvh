# Archivo: impuestos.py

def calcular_impuesto(sueldo):
    """
    Función que calcula el impuesto a pagar (8%) si el sueldo es mayor a 500 soles.
    Si es menor o igual a 500, el impuesto es 0.
    """
    if sueldo > 500:
        impuesto = sueldo * 0.08
        return impuesto
    else:
        return 0.0