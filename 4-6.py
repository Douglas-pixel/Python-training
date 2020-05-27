lista_de_materias =["Matemáticas", "Física", "Química", "Historia", "Lenguaje"]
materias_reprobadas = []

for materia in lista_de_materias:
    nota = int(input("Qué nota tienes en "+ materia + ": " ))
    while nota >10:
        print("No puedes asignar una nota superior a 10")
        nota = int(input("Qué nota tienes en " + materia + ": "))

    if nota <=5:
        materias_reprobadas.append(materia)
    else:
        pass


print("Tendras que repetir la siguientes materias:", materias_reprobadas)