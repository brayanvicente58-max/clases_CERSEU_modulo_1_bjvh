"""Manejo de errores"""
"""
    IndexError:  Evalúa un índice no existente en un lista
"""
def elemento_en(lista, i):
    try:
        return lista[i]
    except IndexError:
        print("Error de índice: {}, está fuera del rango de la lista, su rango es de: 0 a {} ".format(i, len(lista)-1))

nombres = ["Fernando", "Rosa", "Alberto", "Sebastian", "José"]
print(elemento_en(nombres, 1))
print(elemento_en(nombres, 15))