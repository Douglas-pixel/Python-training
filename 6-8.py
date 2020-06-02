import math
def stadistic(*args):
    list = []
    list2 = []
    media = sum(args)/len(args)
    for i in args:
        list.append(i-media)
    for e in list:
        list2.append(e**2)
    varianza = sum(list2)/len(args)
    desviacion =  math.sqrt(varianza)
    return desviacion
numbers = stadistic(600 , 470, 170, 430, 300)
print(numbers)