"""
Uso de librerías de fecha y tiempo
Comparativa de fechas

"""

import datetime


fecha_1 = datetime.datetime(2026,10, 1)
fecha_2 = datetime.datetime(2026,10, 30)

if fecha_1 > fecha_2:
    print("El niño 2 es mayor al niño 1")
elif fecha_1 == fecha_2:
    print("Nacieron el mismo día")
else:
    print("El niño 1 es mayor que el niño 2")