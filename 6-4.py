def Iva(cantidad, porcentaje_de_iva=21):
    return cantidad + (cantidad*(porcentaje_de_iva/100))
calculo = Iva(100)
print(calculo)