palabra =list(input("Introduce una palabra: "))
vowel_a = 0
vowel_e = 0
vowel_i = 0
vowel_o = 0
vowel_u = 0
for letra in palabra:
    if letra == "a":
        vowel_a += 1
    elif letra == "e":
        vowel_e += 1
    elif letra == "i":
        vowel_i += 1
    elif letra == "o":
        vowel_o += 1
    elif letra == "u":
        vowel_u += 1
    else:
        pass
print("tu palabra tiene", vowel_a, "veces la vocal a", vowel_e, "veces la e", vowel_i, "veces la i", vowel_o, "veces la o y",
       vowel_u, " veces la u")
