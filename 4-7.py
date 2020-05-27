abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t","u",
              "v", "w", "x", "y", "z"]
multiplos_de_3 = []
for letra in abecedario:
    posicion = float(abecedario.index(letra))
    posicion+=1
    determination = float(posicion % 3)
    if determination == 0.0:
        multiplos_de_3.append(letra)

for letter in multiplos_de_3:
    abecedario.remove(letter)
print(abecedario)