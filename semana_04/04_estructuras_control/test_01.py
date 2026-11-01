"""Uso de cond. if"""

edad = int(input("Ingrese edad: "))
if 0 < edad < 18:
    print("1. Usted es menor de edad")
elif 18 <= edad < 65:
    print("2. Usted es una persona adulta")
elif 65 <= edad < 100:
    print("3. Usted es un persona adulta de la tercera edad")
else:
    print("4. Usted he ingresado una edad incorrecta, ingrese una edad válida por favor")