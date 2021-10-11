
#remove empty list from list
test_list = [5, 6, [], 3, [], [], 9]
res = [ele for ele in test_list if ele != []]
print(res)

#copy the list
li1 = [4, 8, 2, 10, 15, 18]
li2 = li1[:]
print(li2)


#Times element is present in list
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
print(lst)
counter = 0
for i in lst:
    if( i == 8):
        counter +=1
print("Element Exist times ", counter)


#counter() method 
from collections import Counter
l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)
print(type(d)) 
new_list = list([item for item in d if d[item]>1])
print(new_list)

#sum of number of digits in list
test_list = [12, 67, 98, 34]
res = []
for num in test_list:
    sum = 0
    for i in str(num):
        sum = sum + int(i)
    res.append(sum)

print(res)

