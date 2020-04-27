inv_inicial = int(input("Introduce la cantidad a invertir: "))
tasa_interes = int(input("Introduce la tasa de interés: "))
tiempo = int(input("Introduce la cantidad de años: "))
Total=0
for i in range(0,tiempo):
    inv_inicial= inv_inicial + inv_inicial*(tasa_interes/100)
print(inv_inicial)    