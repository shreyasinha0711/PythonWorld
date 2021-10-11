#remove spaces from string
import re
str1 = "This is a space   check"
str3 = re.sub(' +',' ',str1)
print(str3)
str2 = str1.replace(" ", "")
print(str2)
str4 = " ".join(str1.split())
print(str4)

#max min in tuples
tup = (1, 2, 6, 3)
print(max(tup), min(tup))

#program to access 2nd, 4th, 5th element
lis = [1,"a",2,"b",3,"c"]
indices = (1,3,4)
for i in indices:
    print(lis[i])

#program to reverse element of list
list_a = ["sparta", True, 3+4j, False]
list_a.reverse()
print(list_a)

#program to dict update value of apple from 10 to 25
fruit={"Apple":10,"Orange":20,"Banana":30,"Guava":40}
fruit["Apple"] = 25
print(fruit)

#program to find common between sets
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9}
print(s1.intersection(s2))

#program to print out the 2-table using while loop
n = 2
i = 1
while i < 11:
    print(n, "*", i, "=", n*i)
    i = i+1

#program to find odd or even
def odd_even(n):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

odd_even(21)

#program to print factorial of number
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

factorial = fact(4)
print(factorial)

#program to find palindrome or not

num = 1001
#num = int(input("Enter a num: "))
temp = num
rev = 0
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10

if temp == rev:
    print("palin")
else:
    print("not palin")

#reverse statement
statement = "this is going for reverse"
list_a = list(statement.split(" "))
print(list_a)
list_a.reverse()
print(list_a)
print(" ".join(list_a))

# reverse method 2
sentence = 'geeks quiz practice code'
words = sentence.split(' ')
reverse_sentence = ' '.join(reversed(words))
print(reverse_sentence)

import operator
#frequency of each character in string
test_str = "GeeksforGeeks"
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
#print ("Count of all characters in GeeksforGeeks is :\n "+  str(all_freq))
sorted_freq = dict(sorted(all_freq.items(),key = operator.itemgetter(1),reverse=True))
print(sorted_freq)
#sorted_dict = dict(sorted(all_freq.items(), key = operator.itemgetter(1),reverse = True))

"""program to print the following pattern
1
22
333
4444
55555
"""

for num in range(6):
    for i in range(num):
        print(num, end="")
    print()

"""program to print the following pattern
#
##
###
####
#####
"""
for num in range(6):
    for i in range(num):
        print("#", end="")
    print()


"""program to print the following pattern
    #
   ##
  ###
 ####
#####
"""
num = 5
k = 2*num - 2
for i in range(0, num):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i+1):
        print("# ", end="")
    print("\r")

"""program to print the following pattern
0
01
012
0123
01234
"""
for num in range(0,6):
    for i in range(num):
        print(i, end=" ")
    print()

"""program to print the following pattern
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
number = 1
for num in range(6):
    for i in range(num):
        print(number, end=" ")
        number = number + 1
    print()

"""program to print the following pattern
    #
   ###
  #####
 #######
#########
"""

def pyfunc(r):
    for x in range(r):
        print(' '*(r-x-1)+'#'*(2*x+1))
pyfunc(3)
