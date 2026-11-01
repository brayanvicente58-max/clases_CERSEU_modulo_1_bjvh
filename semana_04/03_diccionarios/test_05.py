# Diccionario inicial de productos
productos = {
    "Laptop": 10,
    "Mouse": 25,
    "Teclado": 15,
    "Monitor": 8
}

# Consultamos un producto con get()
print("Mouse disponibles: {}".format(productos.get("Mouse")))

# Modificamos y agregamos productos con update()
productos.update({
    "Mouse": 30,
    "Webcam": 12
})

#Agregamos un producto solo si no existe
productos.setdefault("Audífonos", 20)

#Eliminamos un producto con pop()
productos.pop("Teclado")

# Mostrar las claves
print("\nProductos:", list(productos.keys()))

# Mostrar las cantidades
print("Cantidades:", list(productos.values()))

# Recorrer el diccionario con items()
print("\nINVENTARIO FINAL")

for nombre, cantidad in productos.items():
    print(nombre, ":", cantidad, "unidades")