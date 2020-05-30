Data = {}
introducir_data = "si"
while introducir_data == "si":
    nombre_del_dato = input("¿Qué dato desea introducir?: ")
    nombre_del_dato = nombre_del_dato.capitalize()
    valor = input(nombre_del_dato + ": ")
    Data[nombre_del_dato] = valor
    print(Data)
    introducir_data = input("¿Agregar más información?(si/no): ")