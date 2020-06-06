def Bin(decimal):
    # Esta función convierte un número decimal a binario
    list1 = []
    while decimal > 1:
        temporal0 = decimal%2
        decimal = decimal/2
        if temporal0 >= 1:
            list1.append("1")
        else:
            list1.append("0")
    list1.reverse()
    sub = "".join(list1)
    return sub
def Dec(binario):
    # esta función convierte un número binario a decimal
    lista = list(str(binario))
    lista.reverse()
    temporal1 = 0
    total = 0
    for i in lista:
        if i >= "1":
            total += 2**temporal1
            temporal1 += 1
        else:
            temporal1 += 1
    return total
print(Dec(100000000))
