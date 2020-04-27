gender = input("Si eres mujer, introduce M y si eres hombre introduce H: ")
name = input("Introduce tu nombre: ")
group = ""
if gender.lower() == "m" and name.lower() < "m":
    group = "A"
else:
    group = "B"
print("Perteneces al grupo:",group)