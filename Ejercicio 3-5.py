amount = int(input("Introduce la cantidad de dinero a invertir: "))
interest = int(input("Introduce el interés: "))
years = int(input("Introduce la cantidad de años a estacionar el dinero: "))
for i in range(0,years):
    amount += float(amount*(interest/100))
    print("En el año,",i+1,"tu cuenta tendrá $",amount)