"""
Ejercicio 10
Participación #3
"""
"""
Uso de cond. if

Uso de if ternarios
Requisitos:
- Ingresar por teclado el sueldo del empleado
- Si el sueldo es mayor que 4000, imprimir "Su sueldo no tiene bonificación"
- Caso contrario indicar: "Su sueldo tiene bonificación este año y será de :
sueldo_final", sueldo_final = sueldo + 20% * sueldo

"""

sueldo = int(input("Ingrese el sueldo del empleado: "))
sueldo_final = sueldo + (0.20 * sueldo)
mensaje = ("Su sueldo no tiene bonificación" if sueldo > 4000 else ("Su sueldo tiene bonificación este año y será de :"f"{sueldo_final}"))

print(mensaje)