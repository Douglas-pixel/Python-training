name = input("Introduce tu nombre: ")
age = input("Introduce tu edad: ")
address = input("Introduce tu dirreción: ")
phone_number = input("Introduce tu número de teléfono: ")
data = {"nombre" : name, "edad" : age, "dirección" : address, "número de teléfono" : phone_number }
print(data["nombre"], "tiene", data["edad"], "su choza está en", data["dirección"], "y su número es",
      data["número de teléfono"])
