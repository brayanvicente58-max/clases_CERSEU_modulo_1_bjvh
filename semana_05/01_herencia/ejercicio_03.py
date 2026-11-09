"""
    Ejercicio 03
    POO
    Tema: Encapsulamiento

    Tipos de atributos:
    - Público:    atributo
    - Protegido:  _atributo
    - Privado:    __atributo
"""


# Clase A: Atributos públicos y protegidos
class A:
    def __init__(self):
        self.inicial = 5
        self._contador = 0

    def incrementa(self):
        self._contador += 1

    def cuenta(self):
        return self._contador


# Clase B: Atributos públicos y privados
class B:
    def __init__(self):
        self.inicial = True
        self.__contador = 0

    def incrementa(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador


#EJEMPLO 1: ATRIBUTO PROTEGIDO
var_1 = A()

print("===== CLASE A =====")
print("Valor inicial: {}".format(var_1.inicial))
print("Contador inicial: {}".format(var_1.cuenta()))

var_1.incrementa()
var_1.incrementa()
var_1.incrementa()

print("Contador final: {}".format(var_1.cuenta()))

# Acceso directo al atributo protegido
print("Acceso a _contador: {}".format(var_1._contador))

# Modificación directa del atributo protegido
var_1._contador = 10
print("Contador modificado: {}".format(var_1.cuenta()))


#EJEMPLO 2: ATRIBUTO PRIVADO
var_2 = B()

print("\n===== CLASE B =====")
print("Valor inicial: {}".format(var_2.inicial))
print("Contador inicial: {}".format(var_2.cuenta()))

var_2.incrementa()
var_2.incrementa()
var_2.incrementa()
var_2.incrementa()

print("Contador final: {}".format(var_2.cuenta()))

#Modificación de un atributo público
var_2.inicial = False
print("Nuevo valor inicial: {}".format(var_2.inicial))

#Acceso directo al atributo privado
#print(var_2.__contador)  # AttributeError

#Acceso mediante "Name Mangling"
print("Acceso interno: {}".format(var_2._B__contador))