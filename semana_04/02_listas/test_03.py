# Lista inicial de productos
productos = ["Laptop", "Mouse", "Teclado", "Monitor", "Impresora"]

# Mostrar los productos registrados
print("INVENTARIO INICIAL")

for producto in productos:
    print(producto)

# Buscar un producto
if "Monitor" in productos:
    print("\nEl producto Monitor está disponible")
else:
    print("\nEl producto Monitor no está disponible")

# Agregar nuevos productos
productos.append("Webcam")
productos.append("Audífonos")

# Eliminar un producto existente
productos.remove("Impresora")

# Reemplazar un producto
indice = productos.index("Mouse")
productos[indice] = "Mouse inalámbrico"

# Ordenar alfabéticamente
productos.sort()

# Mostrar el inventario actualizado
print("\nINVENTARIO ACTUALIZADO")

for producto in productos:
    print(producto)

# Mostrar cantidad total
print("\nTotal de productos:", len(productos))