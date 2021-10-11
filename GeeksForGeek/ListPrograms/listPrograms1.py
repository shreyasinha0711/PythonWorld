#Python program to interchange first and last elements in a list

list_l = [10, 20, 30, 40]
list_l[0], list_l[-1] = list_l[-1], list_l[0]
print(list_l)

#length of list without len and element exists
print(len(list_l))
counter = 0
for i in list_l:
    counter +=1
    if(i == 20):
        print("Element Exist at ", counter)
print("Total Counter: ", counter)

#Different ways to clear a list in Python
list_clear1 = ['a', 'b', 'c']
list_clear1.clear()
print(list_clear1)

list_clear2 = [10, 20, 30]
list_clear2 *= 0
print(list_clear2)

#Reversing a List in Python

list_reverse1 = [10, 'a', 20, 'b']
list_reverse1.reverse()
print("Method 1 Reversed the list ", list_reverse1)

list_reverse2 = [20, 'a', 30, 'b']
reverse2_list = list_reverse2[::-1]
print("Method 2 Reversed the list ", reverse2_list)

#Python program to find sum of elements in list
list_sum1 = [11, 5, 17, 18, 23]
sum1 = 0
sum2 = sum(list_sum1)
for i in list_sum1:
    sum1 = sum1 + i
print("Method 1 The sum of list is ", list_sum1, sum1)
print("Method 2 The sum of list is ", sum2)


#Python program to multiply all values in the
list_mul1 = [11, 5, 17, 18, 23]
mul1 = 1
for i in list_mul1:
    mul1 = mul1 * i
print("Multiply", mul1)

#largest
list_a = [11, 5, 17, 18, 99, 23]
largest = list_a[0]

for i in list_a:
    if i > largest:
        largest = i
print(largest)        

#second largest
list_a = [11, 5, 17, 18, 99, 23]
set_a = set(list_a)
set_a.remove(max(set_a))
print(max(set_a))


#max and second max
list_aa = [11, 5, 17, 18, 99, 23]
aa_max = list_aa[0]
aa_smax = list_aa[0]

for i in range(len(list_aa)):
    if list_aa[i] > aa_max:
        aa_max = list_aa[i]

for i in range(len(list_aa)):
    if list_aa[i] > aa_smax and list_aa[i] != aa_max:
        aa_smax = list_aa[i]

print(f"Max: {aa_max}, SecondMax: {aa_smax}")


#print even in list
list_even = [11, 5, 17, 18, 99, 23]
print([even for even in list_even if even % 2 == 0])

#odd in range
for odd in range(4, 16):
    if odd %2 != 0:
        print(odd, end=" ")
print()

#positive in range
for positve in range(-4, 16):
    if positve >= 0:
        print(positve, end=" ")
print()

#power program
num = 3
k = 4
power_val = 1
for i in range(k):
    power_val = power_val * num

print(f"Power: {power_val}")