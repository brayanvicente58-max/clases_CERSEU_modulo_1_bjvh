"""
Ejercicio 08
Participación"""

""" 
Ejercicio Participación: Manejo de excepciones en listas

**Objetivo:** 
Aplicar el manejo de excepciones en Python para controlar errores al intentar modificar elementos de una lista.

**Requisitos:**

1. Crear una función que reciba dos parámetros: una lista y un índice.
2. Definir una lista que contenga inicialmente **4 elementos numéricos**.
3. Dentro de la función, intentar modificar el elemento correspondiente al índice recibido, asignándole el valor de `0`.
4. Si el índice no existe en la lista, controlar la excepción y agregar un nuevo elemento con el valor de `0` al final de la lista.
5. Mostrar la lista original y la lista final después de ejecutar la función.
6. Realizar dos pruebas:
   - **Caso 1:** Utilizar un índice existente.
   - **Caso 2:** Utilizar un índice que esté fuera del rango de la lista.

**Indicaciones de entrega:**

- Correo: docente.cerseu.unmsm@gmail.com
- Asunto: Participación para práctica 02
- Fecha límite: Domingo 01, hasta las 10:00 p. m.
- Archivos: Enviar en un mismo correo los ejercicios de participación

"""

def modificar_o_agregar(lista, indice):

    try:
        lista[indice] = 0
    except IndexError:
        lista.append(0)

print("=== CASO 1: Utilizar un índice existente ===")
lista_caso1 = [15, 25, 35, 45]
print("Lista original: "f"{lista_caso1}")

modificar_o_agregar(lista_caso1, 2)
print("Lista final: "f"{lista_caso1}\n")


print("=== CASO 2: Utilizar un índice fuera del rango ===")
lista_caso2 = [15, 25, 35, 45]
print("Lista original: "f"{lista_caso2}")

modificar_o_agregar(lista_caso2, 6)
print("Lista final: "f"{lista_caso2}")