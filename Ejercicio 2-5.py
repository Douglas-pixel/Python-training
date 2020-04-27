ingresos = int(input("Introduce tus ingresos mensuales: "))
edad = int(input("Introduce tu edad: "))

if edad >= 16 and ingresos >= 1000:
    print("El usuario tiene que tributar")
else:
    print("El usuaro no tiene que tributar")
