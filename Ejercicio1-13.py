
savings = int(input("introduce la cantidad a ahorrar: "))
years = int(input("introduce la cantidad de años que lo estacionaras: "))
interest = int(input("a que tasa de interés: "))/100
for i in range(0, years):
    savings = (savings + savings*interest)
    print("en el año ",(i+1)," usted tendrá en su cuenta de ahorro: ","{0:.2f}".format(savings)," dólares")
print(2+2)
