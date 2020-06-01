def Cuadrados(*args):
    lista_cuadrados = []
    for i in args:
        calculo = i**2
        lista_cuadrados.append(calculo)
    return lista_cuadrados
lista = Cuadrados(2, 4, 5)
print(lista)