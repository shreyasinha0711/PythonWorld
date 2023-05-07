# Question:
# From a list of numbers, move zero to the end of list

list_a = [1, 0, 2, 0, 4, 6]

for item in list_a:
    if item == 0:
        list_a.remove(item)
        list_a.append(item)

print(list_a)

