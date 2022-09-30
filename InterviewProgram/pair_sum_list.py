#To check and return the pairs of a given array A whose sum value is equal to a target value N

list_n = [1, 2, 4, 9, 11, 5]
a_set = set()
sum = 6
count = 0
for i in range(len(list_n)):
    snum = sum - list_n[i]
    if snum in a_set:
        print(f"[ {list_n[i]}, {snum}]")
        count += 1
    a_set.add(list_n[i])

print(a_set)
print(count)