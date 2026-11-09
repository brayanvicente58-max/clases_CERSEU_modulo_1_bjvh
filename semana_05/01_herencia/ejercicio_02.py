"""
    Ejercicio 02
    Programación Orientada a Objetos (POO)
    Participación

Requerimientos:

- Crear una clase `Alumno`.
- Crear el atributo de clase `nacionalidad` con el valor `"Peruano"`.
- Cada alumno deberá tener un nombre, distrito de residencia y tres calificaciones
correspondientes a los siguientes cursos: Cálculo II, Matemática Discreta, Redes Neuronales
- Las calificaciones deberán estar comprendidas entre 0 y 20. Su valor por defecto será 0 y
podrán proporcionarse como parámetros al instanciar la clase.
- Implementar un método que calcule y muestre el promedio de las tres calificaciones.
- Implementar un método que identifique y muestre el curso con la calificación más alta.
Si existen cursos con la misma calificación máxima, deberán mostrarse todos.
- Implementar un método que determine si el alumno está ""aprobado o desaprobado"",
considera un promedio mínimo aprobatorio de 13.
- Implementar un método que permita mostrar el nombre y distrito de residencia del alumno.
- Crea al menos dos instancias de la clase `Alumno`, utilizando datos y calificaciones distintas.
- Ejecutar los métodos implementados para cada alumno y mostrar sus respectivos resultados.

Consideraciones:
- Se permite utilizar diccionarios para organizar las calificaciones.
- Los resultados deberán mostrarse de forma clara y ordenada.
- No se requiere solicitar información mediante `input()`.

"""


class Alumno:
    nacionalidad = "Peruano"

    def __init__(self, nombre, distrito, calculo_ii=0, matematica_discreta=0, redes_neuronales=0):

        self.nombre = nombre
        self.distrito = distrito

        self.calificaciones = {
            "Cálculo II": self._validar_nota(calculo_ii),
            "Matemática Discreta": self._validar_nota(matematica_discreta),
            "Redes Neuronales": self._validar_nota(redes_neuronales)
        }

    def _validar_nota(self, nota):
        if 0 <= nota <= 20:
            return nota
        print(f"Advertencia: La nota {nota} está fuera del rango [0, 20]. Se asignará 0 por defecto.")
        return 0

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Distrito de Residencia: {self.distrito}")
        print(f"Nacionalidad: {Alumno.nacionalidad}")

    def calcular_promedio(self):
        notas = list(self.calificaciones.values())
        promedio = sum(notas) / len(notas)
        print(f"Promedio de notas: {promedio:.2f}")
        return promedio

    def mostrar_curso_mas_alto(self):
        max_nota = max(self.calificaciones.values())
        cursos_maximos = [curso for curso, nota in self.calificaciones.items() if nota == max_nota]

        print(f"Calificación más alta ({max_nota}): {', '.join(cursos_maximos)}")

    def determinar_estado(self):
        notas = list(self.calificaciones.values())
        promedio = sum(notas) / len(notas)

        if promedio >= 13:
            estado = "Aprobado"
        else:
            estado = "Desaprobado"

        print(f"Estado del alumno: {estado}")
        return estado

    def mostrar_resumen_completo(self):
        print("=" * 45)
        self.mostrar_datos()
        print("-" * 45)
        print("Calificaciones:")
        for curso, nota in self.calificaciones.items():
            print(f"  - {curso}: {nota}")
        print("-" * 45)
        self.calcular_promedio()
        self.mostrar_curso_mas_alto()
        self.determinar_estado()
        print("=" * 45 + "\n")
# Creación de instancias y ejecución del programa

alumno1 = Alumno("Carlos Mendoza", "Miraflores", calculo_ii=16, matematica_discreta=14, redes_neuronales=18)
alumno2 = Alumno("Ana Torres", "San Isidro", calculo_ii=15, matematica_discreta=11, redes_neuronales=15)
alumno3 = Alumno("Luis Gómez", "Surco", calculo_ii=10)

# Ejecución de métodos para cada alumno
alumno1.mostrar_resumen_completo()
alumno2.mostrar_resumen_completo()
alumno3.mostrar_resumen_completo()