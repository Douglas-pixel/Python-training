diccionario = {"dolar" : "$", "yen": "simbolo de yen", "euro" : "simbolo de euro"}
pregunta = input("¿De qué divisa quieres saber el símbolo?: ")
if pregunta not in diccionario:
    print("no le manejamos esa divisa")
else:
    print(diccionario[pregunta])


