cesta = {}
continuar = "si"
total = 0
while continuar == "si":
    articulo = input("¿Qué artículo deseas comprar?: ")
    precio = float(input("Precio de {}: ".format(articulo)))
    cesta[articulo] = precio
    continuar = input("¿Desea añadir otro artículo?(si/no): ")
total = sum(cesta.values())
for producto in cesta:
    print(producto, "$" + str(cesta[producto]))
print("el total es $" + str(total))