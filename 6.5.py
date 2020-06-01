def CircleArea(radio):
    return 3.1416*(radio*radio)
def Volumen(altura, radio):
    return altura*CircleArea(radio)


input = float(Volumen(10,5))
print("El volumen de tu cilindro es {}".format(input))
