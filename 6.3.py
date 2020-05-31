def factorial (number):
    number_list = []
    for i in range (1, int(number)):
        number_list.append(i)
    for i in number_list:
        number = i*number

    return number
print(factorial(10))