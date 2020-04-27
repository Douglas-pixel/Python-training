Barras_compradas_no_frescas= int(input("Introduce la cantidad de barras compradas no frescas: "))
coste = 3.49
print("El precio por barra fresca es de $3.49")
print("El descuento por no ser del día es $",(Barras_compradas_no_frescas*coste)*0.6)
print("El coste total es $","{0:.2f}".format((Barras_compradas_no_frescas*coste)*0.4))
