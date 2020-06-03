def Contador(texto):
    lista0 = texto.split()
    diccionario0 = {}
    for i in lista0:
        variable_temporal0 = lista0.count(i)
        diccionario0[i] = variable_temporal0
    return diccionario0
def MostRepeated(texto2):
    nueva_lider = None
    variable_temporal1 = 0
    diccionario3 = Contador(texto2)
    for i  in diccionario3:
        value = diccionario3[i]
        nueva_lider = None
        if value>variable_temporal1:
            variable_temporal1 = value
            nueva_lider = i
    if nueva_lider == None:
        return "No hay palabra más repetida, pero sí hay palabraS más repetidaS"
    else:
        return nueva_lider, variable_temporal1

words = MostRepeated(input("""Escibe aquí algún texto:
 """))

print(words)