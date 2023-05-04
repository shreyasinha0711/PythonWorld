# Take the input from user
# Append in the empty list
# Find its average rounding to 2 digits


n = int(input("Enter the number of inputs: "))
a = []

for i in range(n):
    item =  int(input("Enter the number: "))
    a.append(item)

average = sum(a)/n
print(average)
print(round(average, 2))
