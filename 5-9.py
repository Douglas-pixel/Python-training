facturas = {}
total = 0
total2 = 0
consulta = 0
continuar = "si"
while continuar == "si":
    consulta = int(input("Escriba 1  si quiere añadir factura, escriba 2 si quiere pagar factura y 3 si quiere terminar: "))
    if int(consulta) == 1:
        var1 = int(input("Introduce número de la factura: "))
        var2 = float(input("Introduce valor de la factura: "))
        facturas[var1] = var2
        print("Cantidad por pagar {}".format(sum(facturas.values())))
        print("El total pagado es {}".format(float(total2)))
        continuar =input("¿Desea continuar?(si/no)")
    elif int(consulta) == 2:
        var3 = int(input("Introduce el número de la factura a borrar: "))
        total2 += facturas[var3]
        facturas.pop(var3)
        print("Cantidad por pagar {}".format(sum(facturas.values())))
        print("El total pagado es {}".format(float(total2)))
        continuar = input("¿Desea continuar?(si/no)")
    elif int(consulta) == 3:
        continuar = "ain´t"
        print("Proceso finalizado")




