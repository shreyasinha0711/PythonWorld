#enumerate is used to join the list with number
print("-----ENUMERATE----")

friends = ["Rolf", "Charlie", "Jen"]

for counter, friend in enumerate(friends, start=1):
    print(f" {counter} {friend}")

print(list(enumerate(friends)))
print(dict(enumerate(friends)))
print(list(zip([0,1,2], friends)))


