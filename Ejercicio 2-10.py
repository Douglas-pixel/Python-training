ingrediente =""
tipodepizza =input("¿Quieres pizza vegetariana o tradicional?: ")
if tipodepizza.lower() =="vegetariana":
    ingrediente= input("Puede incluir 1 de los siguientes ingredientes: pimiento y tofu ")
else:
    ingrediente = input("puede incluir 1 de los siguientes ingredientes: Peperoni, Jamón y Salmón ")

print("Su pizza es ",tipodepizza,"y lleva mozzarella, tomate y",ingrediente)