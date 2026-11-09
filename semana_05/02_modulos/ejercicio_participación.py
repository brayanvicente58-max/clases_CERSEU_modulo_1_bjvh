"""Intervención"""
"""Ejercicio módulos"""
"""
Requisitos:
    1. Crea un módulo donde se va a tener una función que obtiene el impuesto
    que va a pagar una persona si el sueldo es mayor a 500 soles, impuesto: 8%
    2. Ingresar el sueldo po consola, va a estar en un archivo principal
    Entregar solución al correo: docente.cerseu.unmsm@gmail.com
    
    Asunto: Participación  - Examen final

"""

# Importamos la función desde nuestro módulo creado
from impuesto import calcular_impuesto

def main():
    print("--- Cálculo de Impuesto por Sueldo ---")
    try:
        # Ingresar el sueldo por consola[cite: 2]
        sueldo_ingresado = float(input("Ingrese el sueldo de la persona (en soles): "))
        if sueldo_ingresado < 0:
            print("El sueldo no puede ser negativo.")
            return
        # Obtenemos el impuesto llamando a la función del módulo[cite: 2]
        monto_impuesto = calcular_impuesto(sueldo_ingresado)
        # Mostramos los resultados de forma clara y ordenada
        print(f"\nSueldo ingresado: S/. {sueldo_ingresado:.2f}")
        if sueldo_ingresado > 500:
            print(f"El sueldo supera los 500 soles.")
            print(f"El impuesto a pagar (8%) es: S/. {monto_impuesto:.2f}")
            print(f"Sueldo neto restante: S/. {(sueldo_ingresado - monto_impuesto):.2f}")
        else:
            print("El sueldo es de 500 soles o menos, por lo tanto, no aplica el impuesto del 8%[cite: 2].")
    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido para el sueldo.")
if __name__ == "__main__":
    main()