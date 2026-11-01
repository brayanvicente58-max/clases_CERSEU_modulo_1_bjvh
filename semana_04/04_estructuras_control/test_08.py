"""
Uso del búcle for
Lista
"""
ingenierias = ["Sistemas", "Software", "Mecánica", "Industrial", "Electrónica"]
ing_extras = ["Mecatrónica", "Civil" ]

for ingeniera in ingenierias:
    print("Ingeniería {}".format(ingeniera))

ingenierias.extend(ing_extras)

print("Lista actualizada:")
for ingeniera in ingenierias:
    print("Ingeniería {}".format(ingeniera))