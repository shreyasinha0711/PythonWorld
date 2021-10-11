#frequency of char in string
import operator
str1 = "shreyasherrr"
all_freq1 ={}

for i in str1:
    if i in all_freq1:
        all_freq1[i] += 1
    else:
        all_freq1[i] = 1

print(all_freq1)
#sort
sorted_freq1 = dict(sorted(all_freq1.items(), key= operator.itemgetter(1),reverse= False))
print(sorted_freq1)


#first repetative char
str2 = "shreyasherrr"
all_freq2 ={}

for i in str2:
    if i in all_freq2:
        print(i)
        break
        #return i
    else:
        all_freq2[i] = 1 


#first non repetative char
from collections import Counter
str3 = "shreyasherrr"
freq = Counter(str3)

for i in str3:
    if freq[i] == 1:
        print(i)
        break

#recursive
def rev_str(stra):
    if len(stra) == 0:
        return stra
    else:
        return rev_str(stra[1:]) + stra[0]

#string program
str_space ="This has     a   lot "
print(' '.join(str_space.split()))

#string program--reverse
str_rev =""
for i in str1:
    str_rev =i + str_rev

print(str_rev)

str_rev1 = str1[::-1]
print(str_rev1)

str_rev2= "".join(reversed(str1))
print(str_rev2)


str_sent = "this is a boy"
words = str_space.split()
rev_sent = " ".join(reversed(words))
print(rev_sent)

#fib
n1 = 0
n2 = 1

def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i))


#anagrams
