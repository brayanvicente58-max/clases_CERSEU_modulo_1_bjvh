"""Uso del búcle While"""
"""Utilizando: break"""

numero = 1
print("Los números inician con: {}".format(numero))
while True:
    print("numero: ", numero)
    #numero += 1
    numero = numero + 1
    if numero > 10:
        print("Aquí se detiene el bucle porque el máximo número a comparar es 10")
        break