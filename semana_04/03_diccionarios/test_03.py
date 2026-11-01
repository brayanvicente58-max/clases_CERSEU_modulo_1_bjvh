# Diccionario de inventario
inventario = {
    "Laptop": 10,
    "Mouse": 25,
    "Teclado": 15,
    "Monitor": 8,
    "Impresora": 5
}

# Consultar cantidad de laptops
print("Laptops disponibles:", inventario["Laptop"])

#Agregamos un nuevo producto
inventario["Webcam"] = 12

#Modificamos la cantidad de Mouse
inventario["Mouse"] = 30

#Descontamos 3 teclados vendidos
inventario["Teclado"] -= 3

#Verificamos si existe Monitor en los registros del inventario
if "Monitor" in inventario:
    print("Monitor está registrado")

#Recorremos las claves del diccionario
print("\nINVENTARIO ACTUALIZADO: ")
for producto in inventario:
    print(producto, ":", inventario[producto], "unidades")