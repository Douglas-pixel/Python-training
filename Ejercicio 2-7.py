usertaxes = int(input("Introduce la tu cantidad de renta anual: "))
if usertaxes < 10000:
    print(" Tu tipo impositivo es 5%")
elif usertaxes  < 20000 :
    print("Tu tipo impositivo es 15%")
elif usertaxes < 35000:
    print("Tu tipo impositivo es 20% ")
elif usertaxes < 60000:
    print("Tu tipo impositivo es 30%")
elif usertaxes > 6000:
    print("Tu tipo impositivo es 45%")