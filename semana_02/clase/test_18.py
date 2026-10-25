"""
1. Crear 2 variables enteras, 2 variables flotantes, 2 variables string, 1 variable string que contiene
valor numérico y una variable boolean
2. Obtener y mostrar la suma de una variable entera con una variables string numérica
(Realizar conversión si fuera necesario)
3. Obtener y mostrar la suma de las 2 variables enteras más la variable string numérica
y la variable flotante
4. Obtener y mostrar el módulo de las variables enteras: %
5. Obtener y mostrar el resultado de las parte entera, usando las varaibles enteras: //
6. Obtener una potencia usando una de las variables flotantes como base y
una variable entera como potencia

Nota: Las variables string pueden ser tu nombre y apellido

"""
var_1 = 400
var_2 = 8
nombre = "Camila"
apellido = "Vicente"
var_3 = 12.25
var_4 = 3.5
var_5 = "1926"
var_6 = True

suma_1 = var_1 + int(var_5)
print(suma_1)
print("-------------------")
suma_2 = var_1 + var_2 + int(var_5) + var_3
print(suma_2)
print("-------------------")
módulo_1 = var_1 % var_2
print(módulo_1)
print("-------------------")
div_entera= var_1 // var_2
print(div_entera)
print("-------------------")
potencia_1 = var_4 ** var_2
print(potencia_1)