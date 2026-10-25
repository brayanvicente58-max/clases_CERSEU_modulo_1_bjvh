"""
Listas en Python

copy(): Copia todos los elementos de una lista a otra nueva lista

"""

var_1 = ["SQLServer", "Sass", "RDS", "Mysql", "Postgresql", "MaríaDB"]

var_1_copy = var_1.copy()

print("Elementos de mi nueva lista: {}".format(var_1_copy))

var_1_copy.append("SQLite3")
var_1_copy.append("33")
var_1_copy.pop(1)

print("Mi lista clon actualizada es: {}".format(var_1_copy))

print(var_1)