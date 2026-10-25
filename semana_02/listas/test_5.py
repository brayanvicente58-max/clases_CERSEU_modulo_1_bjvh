"""
Listas en Python

remove(): Elmina un elemento de la lista, indicando el valor

"""
tecnologias = ["Python", "Java", "C++", "PHP", "Typescript", "Javascript"]
print(tecnologias)

tecnologias.remove("Python")

print("Mi lista actualizada", tecnologias)

tecnologias.remove("Java")
print("Mi lista actualizada", tecnologias)

#Los cambios aplicados con remove se mantienen
print(tecnologias)