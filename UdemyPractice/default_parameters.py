def add(x, y):
    total = x + y
    return total

print(add(5, 10))


def add(x, y=3): #y=3 is default parameter
    total = x + y
    return total

print(add(x=5, y =2)) #named arguments
#print(add(x=5, 2)) can't be used as first has name and 2nd can't
# first can't have and other have is fine add(5, y=2)

#def add(x= 5, y) gives error as non-default agrument follows default argument

print(1, 2, 3, 4, 5, sep=" -")

