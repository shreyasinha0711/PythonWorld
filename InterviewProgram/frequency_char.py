import operator

string_input = input("Enter the String: ")
all_freq = {}

for c in string_input:
    if c in all_freq:
        all_freq[c] += 1
    else:
        all_freq[c] = 1


print(all_freq)


#sort the output based on value
sorted_freq = dict(sorted(all_freq.items(), key = operator.itemgetter(1), reverse = False))
print(sorted_freq)


#find the first repetative character in word

for c in string_input:
    if c in all_freq:
        print(f"The first repetative character is {c}")
        break
    else:
        all_freq[c] = 1


#first non repetative character in word

from collections import Counter
freq = Counter(string_input)

for c in string_input:
    if freq[c] == 1:
        print(f"The first non repetative character is {c}")
        break



