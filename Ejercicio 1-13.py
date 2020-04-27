investment = int(input("Introduce la cantidad a invertir: "))
tasa_interes = int(input("Introduce la tasa de interés: "))
tiempo = int(input("Introduce la cantidad de años: "))
Total=0
for i in range(0,tiempo):
    investment= investment + investment*(tasa_interes/100)
    print("En el año",i+1,"su dinero será:","{0:.2f}".format(investment))
