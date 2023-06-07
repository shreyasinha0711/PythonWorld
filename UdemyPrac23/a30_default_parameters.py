def add(x, y=3):
    total = x + y
    return total


print(add(5, 10))
print(add(5))

print(add(x=4))  # named parameter, for better understanding

print(add(x=4, y=3))

# print(add(x=5, 2)) error first has name, second one should have name.

print(1, 2, 3, 4, 5, sep="-")

