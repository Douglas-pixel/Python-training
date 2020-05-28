fruits_prices = {"plátano": 1.35, "manzana": 0.80, "pera" : 0.85, "naranja" : "0.70"}
consulta1 = input("¿Qué fruta quieres? ")
consulta2 = input("¿Cúantos kilos deseas llevar? " )
if consulta1 in fruits_prices:
    respuesta = fruits_prices[consulta1]*float(consulta2)
    print("EL precio sería de:", respuesta, "dólares" )
else:
    print("no tenemos en stock esa fruta")
