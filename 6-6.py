def Media(*args):
    total=0
    for i in args:
        total +=i
    return total/len(args)
numbers = Media(60, 60, 60, 4)
print(numbers)
