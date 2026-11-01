"""
Ejercicio 04
Intervención
"""
"""
Intervención

Requisitos:
- Dentro de una empresa se va solicitar pedir el nombre y apellido del empleado (input)
- Distrito de residencia ingresado por teclado
- Sueldo y cálculo del bono final de año: que será el triple del sueldo mensual menos el 10% del sueldo
- Todos estos datos se van a ingresar a un diccionario
- Asignar a 3 variables los valores del diccionario
- Mostrar por la terminal (output) el mensaje de: "'Nombre' 'Apellido', recibirá 'bono' soles de fin de año"
"""

nombre = input("Ingrese el nombre del empleado: ")
apellido = input("Ingrese el apellido del empleado: ")
distrito = input("Ingrese el distrito de residencia: ")
sueldo = int(input("Ingrese el sueldo del empleado: "))

bono = (3 * sueldo) - (0.10 * sueldo)

empleado_dict = {"nombre": nombre, "apellido": apellido, "distrito": distrito, "sueldo": sueldo, "bono": bono,}

v_nombre = empleado_dict["nombre"]
v_apellido = empleado_dict["apellido"]
v_bono = empleado_dict["bono"]

print(f"'{v_nombre.title()}' '{v_apellido.title()}', recibirá '{v_bono}' soles de fin de año")