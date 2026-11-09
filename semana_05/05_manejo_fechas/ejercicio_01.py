from datetime import datetime

#str_date = "2-10-2025"
str_date = "2026/10/2"

"""
d: día
m: mes
Y: año
"""

#conversion = datetime.strptime(str_date, "%d-%m-%Y")
conversion = datetime.strptime(str_date, "%Y/%m/%d")

print(conversion)
print(type(conversion))

"""Traer el mes de la fecha con formato letra: strftime de datetime"""
conversion_mes = datetime.strftime(conversion, "%d %b del %Y")
print(conversion_mes)

"""
    b: reemplaza a 'm' para mostrar el mes de forma literal
"""