palabra = input("Introduce una palabra para ver si es palíndromo: ")
palabra_normal = []
palabra_al_reverso  = []
for letra in palabra:
    palabra_normal.append(letra)
for letra1 in palabra_normal:
    palabra_al_reverso.append(letra1)
palabra_al_reverso.reverse()
if palabra_normal == palabra_al_reverso:
    print("Esta palabra es palíndromo")
else:
    print("esta palabra no es palíndromo")

