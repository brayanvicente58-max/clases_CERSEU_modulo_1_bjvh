"""
Listas en Python

count(): Cantidad de veces que se repite un elemento dentro de la lista

"""

tecnologias = ["Python", "Java", "C++", "PHP", "Typescript", "Javascript"]

tecnologias.append("Python")
tecnologias.append("Python")
tecnologias.append("Python")
tecnologias.append("Python")
tecnologias.append("NodeJS")
print("Mi lista actualizada: {}".format(tecnologias))

print("Cantidad de veces que se repite 'Python': {}".format(tecnologias.count("Python")))
print("Cantidad de veces que se repite 'Java': {}".format(tecnologias.count("Java")))